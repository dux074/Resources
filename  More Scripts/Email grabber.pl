#!/usr/bin/perl -w
# Email grabber!
# Coded by: Saime
# Website: http://saime.biz

require LWP::UserAgent;
my $connection = LWP::UserAgent->new;
$connection->agent('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.3) Gecko/20070309 Firefox/2.0.0.4');
$connection->timeout(10);
my $google = "http://www.google.com/search?hl=en&q=mail"; # The search engine , you can add more , or edit it to another like altavista/search[dot]com/etc ...
my @dorks = shift || ("mailto:*\@aol.com"); # Add the dorks here ....
my @pages = shift || ("&start=","&start=10","&start=20","&start=30","&start=40","&start=50","&start=60","&start=70","&start=80","&start=90","&start=100");

my $file;
request(0);
 
sub request {
    print "searching url -> $google";
    for(my $count = 0;$count<=$#dorks;$count++){
    my $url = $google . $dorks[$count] . $pages[1] . "$_[0]"; # where the pages is , edit [1] to [2] or [3] , like that up to [10]
    my $response = $connection->get($url);
    my $con = $response->content;

    while($con =~ m/<td class="(.*?)"><font size=-1>(.*?)mailto:(\w*\@\w*\.\w*)(.*?)<span class=a>/g){
    my $email = "$3";
    print "[+] Found email: " . "$email\n";
}
      shift(@dorks);
      request(0)
}
}