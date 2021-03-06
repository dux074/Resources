#!/usr/bin/perl
#
#
# Simple PHP BB version checker
use LWP::UserAgent;

# set useragent 
$useragent = LWP::UserAgent->new;


# website
$site = $ARGV[0];
#
# get the changelog
$res = $brows->get($site.'/docs/CHANGELOG.html');
if($res->is_success) {
    @ver=$res->content=~/<li><a href="(.*?)\">Changes since (.*?)<\/a><\/li>/i;
    $ver[1]=~/(\d+)\.(\d+)\.(\d+)/;
    $version=$1.'.'.$2.'.'.scalar $3+1;
    print 'Version: '.$version if $version; 
}

