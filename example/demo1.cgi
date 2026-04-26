#!/usr/bin/perl -w

# uncomment this when doing maintenance work:
# print "Content-Type: text/html\n\n";
# print "Database temporarily disabled for maintenance.<br>\n";
# exit;

use lib "/tmp/releases/gedafe/lib/perl";

use Gedafe::Start;
use CGI qw~:standard~;
$|=1; # do not buffer output to get a more responsive feeling

my $cgi = CGI->new;

Start(
    $cgi , 
    db_datasource  => 'DBI:Pg:dbname=gedafedemo1',
    list_rows      => 15,
    templates      => '/tmp/releases/gedafe/example/templates',
    schema	   => 'public',
    schema_search_path => " 'public' ",     
    pearl_dir      => '/tmp/releases/gedafe/example/mypearls',
    widget_dir      => '/tmp/releases/gedafe/example/mywidgets',
    oyster_dir      => '/tmp/releases/gedafe/example/myoysters',
    isearch        => 'java/isearch.jar',
    show_row_count => 0,
    edit_buttons_left => 0,
);
