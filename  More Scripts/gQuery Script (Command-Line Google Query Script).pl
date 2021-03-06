#!/usr/bin/perl
#
#######################################
#         ___                         #
#   __ _ / _ \ _   _  ___ _ __ _   _  #
#  / _` | | | | | | |/ _ \ '__| | | | #
# | (_| | |_| | |_| |  __/ |  | |_| | #
#  \__, |\__\_\\__,_|\___|_|   \__, | #
#  |___/                       |___/  #
#                                     #
#  Command-Line Google Query Script   #
#  Written By: Captain Box (captbox)  #
#######################################
my $gQueryVersion = "0.4";

use strict;
use LWP::UserAgent;
use Getopt::Std;
use URI::Escape;
use HTML::Entities;

# Settings #
my $sGoogleHost = "www.google.com";
my $iMaxResults = 5;
my $bVerbose = 0;
my $bSummaries = 0;
my $bTitles = 0;
my $iPageNum = 1;
my $Query = '';
my $iPageOffset = 0;
my $iReturnedResults = 0;
my $sRequestURL = '';
my $UserAgent;
my $ReturnedData;
my $ReturnedPage;
my $AgentString = '';

sub usage()
{
	print STDERR << "EOU";
gQuery v$gQueryVersion (Google Query Tool)
Written by: Captain Box (captbox)
usage: $0 [-hvftsrpHU] [options] <query>
 -h		: Display this help.
 -v		: Verbose output.
 -f		: Return only first result. (Equiv: '-r 1')
 -t		: Print result titles.
 -s		: Print result summaries.
 -r <number>	: Number of results to return. (Default: 5)
 -p <page>	: Page number to return results from. (Default: 1)
 -H <host>	: Google hostname to use. (Default: www.google.com)
 -U <agent>	: User-Agent string to use. (Default: Firefox 2.0)
  		  WARNING: Changing this may break the script!
EOU
	exit(1);
}
#
my %opt=();
getopts("hvftsr:H:p:U:", \%opt) or usage();
usage() if $opt{h};
usage() if not $ARGV[0];

$bVerbose++ if $opt{v};
$bSummaries++ if $opt{s};
$bTitles++ if $opt{t};
$iMaxResults = 1 if $opt{f};

$iMaxResults = $opt{r} if $opt{r};
$sGoogleHost = $opt{H} if $opt{H};
$iPageNum = $opt{p} if $opt{p};

# This user-agent is hard-coded right now because Google seems to 
# return different formatting based on the user-agent given.
$AgentString = "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20070219 BonEcho/2.0.0.1";
$AgentString = $opt{U} if $opt{U};

$Query = uri_escape($ARGV[0]);

# Sanity Checks ;-) #
if($iMaxResults > 100)
{
	print "WARNING: iMaxResults too big($iMaxResults)! Using 100.\n" if $bVerbose;
	$iMaxResults = 100;
}

if($iMaxResults <= 0)
{
	print "WARNING: iMaxResults <= 0! Using 1.\n" if $bVerbose;
	$iMaxResults = 1;
}

if($iPageNum <= 0)
{
	print "WARNING: iPageNum <= 0! Using 0.\n" if $bVerbose;
	$iPageNum = 0;
}
# End idiot proofing. :-P #

$iPageOffset = $iMaxResults * ($iPageNum - 1);

$sRequestURL = "http://${sGoogleHost}/search?num=${iMaxResults}&start=${iPageOffset}&q=${Query}";
print "Request URL: $sRequestURL\n" if $bVerbose;

print "Sending request..." if $bVerbose;
$UserAgent = new LWP::UserAgent;
# View note above about user-agents.
# $UserAgent->agent("gQuery/$gQueryVersion");
$UserAgent->agent($AgentString);
$ReturnedData = $UserAgent->get($sRequestURL);
$ReturnedPage = $ReturnedData->content;
print "Done!\n" if $bVerbose;

if($ReturnedPage =~ m/<br>Your search - <b>.*?<\/b> - did not match any documents.  <br>/)
{
	print "No matches.\n";
	exit(0);
}
$ReturnedPage =~ s/(\n|\r)//g;

my $Result_url;
my $Result_title;
my $Result_desc;
my $Result;
my $ResultCounter = 0; 

while($ReturnedPage =~ m/<!--m-->(.*?)<!--n-->/ig)
{
	$Result = $1;
	if($Result =~ m/<h2[^>]*><a.*?href="([^"]*?)".*?>(.*?)<\/a><\/h2>.*?<font size=-1>(.*?)<span/ig)
	{
                $Result_url = $1;
                $Result_title = $2;
                $Result_desc = $3;

		$Result_title = decode_entities($Result_title);
		$Result_desc = decode_entities($Result_desc);

		print "$Result_title: " if $bTitles;
		print $Result_url;
		print " - $Result_desc" if $bSummaries;
		print "\n";

		$ResultCounter++;
	}
}

print "Returned results: $ResultCounter\n" if $bVerbose and $ResultCounter > 0;

if($ResultCounter == 0)
{
	print "No matches.\n";
	exit(0);
}
