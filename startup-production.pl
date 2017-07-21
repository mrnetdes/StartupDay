#!/usr/bin/perl
use warnings; #looks_like_number()
use strict;

use Win32::Console::ANSI;
use Term::ANSIColor;
use Net::LPR; #used for printing
use Sys::Hostname; #used for printing
use Data::Dumper;
use DBI; #used for mysql functionality

# update

my $AskColor = "yellow";


#--------------------------------------------------------
# Class: Person
#--------------------------------------------------------
package Person;

sub new
{
    my $class = shift;
    my $self = {
        _userid => shift,
        _fname => shift,
        _lname => shift,
        _propername => shift,
        _year => shift,
        _enrollyear => shift,
        _yearbookQ => 0,
        _yearbookA => 0,
        _lanyardQ => 0,
        _lanyardA => 0,
        _pacduesQ => 0,
        _pacduesA => 0,
        _spiritlifeQ => 0,
        _spiritlifeA => 0,
        _otherQ => 0,
        _otherA => 0,
        _cafe => 0,
        _total => 0,
    };

    bless $self, $class;
    return $self;
}

#----------------------------------------------------
sub get_userid {
    my( $self ) = @_;

    return $self->{_userid};
}
sub set_userid {
    my ( $self, $userid ) = @_;
    $self->{_userid} = $userid if defined($userid);

    return $self->{_userid};
}
#----------------------------------------------------
sub get_fname {
    my( $self ) = @_;

    return $self->{_fname};
}
sub set_fname {
    my ( $self, $fname ) = @_;
    $self->{_fname} = $fname if defined($fname);

    return $self->{_fname};
}
#----------------------------------------------------
sub get_lname {
    my( $self ) = @_;

    return $self->{_lname};
}
sub set_lname {
    my ( $self, $lname ) = @_;
    $self->{_lname} = $lname if defined($lname);

    return $self->{_lname};
}
#----------------------------------------------------
sub get_propername {
    my( $self ) = @_;

    return $self->{_propername};
}
sub set_propername {
    my ( $self, $propername ) = @_;
    $self->{_propername} = $propername if defined($propername);

    return $self->{_propername};
}
#----------------------------------------------------
sub get_year {
    my( $self ) = @_;

    return $self->{_year};
}
sub set_year {
    my ( $self, $year ) = @_;
    $self->{_year} = $year if defined($year);

    return $self->{_year};
}
#----------------------------------------------------
sub get_enrollyear {
    my ( $self) = @_;

    return $self->{_enrollyear}; 
}
sub set_enrollyear {
    my ( $self, $enrollyear) = @_;
    $self->{_enrollyear} = $enrollyear if defined($enrollyear);

    return $self->{_enrollyear};
}
#----------------------------------------------------
sub get_yearbookQ {
    my( $self ) = @_;

    return $self->{_yearbookQ};
}
sub set_yearbookQ {
    my ( $self, $yearbookQ ) = @_;
    $self->{_yearbookQ} = $yearbookQ if defined($yearbookQ);

    return $self->{_yearbookQ};
}
#----------------------------------------------------
sub get_yearbookA {
    my( $self ) = @_;

    return $self->{_yearbookA};
}
sub set_yearbookA {
    my ( $self, $yearbookA ) = @_;
    $self->{_yearbookA} = $yearbookA if defined($yearbookA);

    return $self->{_yearbookA};
}
#----------------------------------------------------
sub get_lanyardQ {
    my( $self ) = @_;

    return $self->{_lanyardQ};
}
sub set_lanyardQ {
    my ( $self, $lanyardQ ) = @_;
    $self->{_lanyardQ} = $lanyardQ if defined($lanyardQ);

    return $self->{_lanyardQ};
}
#----------------------------------------------------
sub get_lanyardA {
    my( $self ) = @_;

    return $self->{_lanyardA};
}
sub set_lanyardA {
    my ( $self, $lanyardA ) = @_;
    $self->{_lanyardA} = $lanyardA if defined($lanyardA);

    return $self->{_lanyardA};
}
#----------------------------------------------------
sub get_pacduesQ {
    my( $self ) = @_;

    return $self->{_pacduesQ};
}
sub set_pacduesQ {
    my ( $self, $pacduesQ ) = @_;
    $self->{_pacduesQ} = $pacduesQ if defined($pacduesQ);

    return $self->{_pacduesQ};
}
#----------------------------------------------------
sub get_pacduesA {
    my( $self ) = @_;

    return $self->{_pacduesA};
}
sub set_pacduesA {
    my ( $self, $pacduesA ) = @_;
    $self->{_pacduesA} = $pacduesA if defined($pacduesA);

    return $self->{_pacduesA};
}
#----------------------------------------------------
sub get_spiritlifeQ {
    my( $self ) = @_;

    return $self->{_spiritlifeQ};
}
sub set_spiritlifeQ {
    my ( $self, $spiritlifeQ ) = @_;
    $self->{_spiritlifeQ} = $spiritlifeQ if defined($spiritlifeQ);

    return $self->{_spiritlifeQ};
}
#----------------------------------------------------
sub get_spiritlifeA {
    my( $self ) = @_;

    return $self->{_spiritlifeA};
}
sub set_spiritlifeA {
    my ( $self, $spiritlifeA ) = @_;
    $self->{_spiritlifeA} = $spiritlifeA if defined($spiritlifeA);

    return $self->{_spiritlifeA};
}
#----------------------------------------------------
sub get_otherQ {
    my( $self ) = @_;

    return $self->{_otherQ};
}
sub set_otherQ {
    my ( $self, $otherQ ) = @_;
    $self->{_otherQ} = $otherQ if defined($otherQ);

    return $self->{_otherQ};
}
#----------------------------------------------------
sub get_otherA {
    my( $self ) = @_;

    return $self->{_otherA};
}
sub set_otherA {
    my ( $self, $otherA ) = @_;
    $self->{_otherA} = $otherA if defined($otherA);

    return $self->{_otherA};
}
#----------------------------------------------------
sub get_cafe {
    my( $self ) = @_;

    return $self->{_cafe};
}
sub set_cafe {
    my ( $self, $cafe ) = @_;
    $self->{_cafe} = $cafe if defined($cafe);

    return $self->{_cafe};
}
#----------------------------------------------------
sub update_total {
    my( $self ) = @_;
    $self->{_total} = $self->{_yearbookA} + $self->{_lanyardA} + $self->{_pacduesA} + $self->{_spiritlifeA} + $self->{_otherA} + $self->{_cafe};

    return $self->{_total};
}
sub get_total {
    my( $self ) = @_;

    return $self->{_total};
}

















#--------------------------------------------------------
# Returns input from the user 
#--------------------------------------------------------
sub get_input {
    my $message = shift;
    print $message;
    chomp(my $userInput = <STDIN>);
        
    return uc($userInput);
}

#--------------------------------------------------------
# Checks if Student Number is in Startup Database
#--------------------------------------------------------
sub mysql_check {
    my $user = shift;

    return 1;
}

#--------------------------------------------------------
# Gets number of seconds from midnight of that day
#--------------------------------------------------------
sub midnight_seconds {
    my @time = localtime();
    my $secs = ($time[2] * 3600) + ($time[1] * 60) + $time[0];

    return $secs;
}

#--------------------------------------------------------
# Clears the current window
#--------------------------------------------------------
sub clear_screen {
    if ($^O eq 'MSWin32') {
        system('cls');
    }
    else {
        system('clear');
    }
}

#--------------------------------------------------------
# Stores off a receipt to a log file
#--------------------------------------------------------
sub store_receipt {
    my $filename = shift;
    my $data = shift;

    open(my $fh, '>', 'Logs/'.$filename.'.txt') or die("\n\n==ERROR== storing file: $filename.txt");
    print $fh "$data";
    close $fh;
}

sub show_totals {
    my (%users) = @_;
    my $grand_total = 0;

    #--------------------------------------------------------
# Creating Receipt
#--------------------------------------------------------
# -Creating Header-
use POSIX qw(strftime);
my $receipt = "";

#CR
#my $datestring = strftime '%x %X',localtime(); # getting date and time
my $datestring = substr(localtime(),4);


my $receipt_header = "--LCHS STARTUP DAY--\n$datestring\n\n";
$receipt .= $receipt_header; # appending header to main receipt

# -Creating Body-
# Looping through all users getting necessary information for receipt
keys %users; # reset the internal iterator so a prior each() doesn't affect the loop
while(my($k, $v) = each %users) {
    $users{$k}->update_total(); # making sure totals are up to date

    # Retrieving a user's information
    my $lname       = $users{$k}->get_lname();
    my $propername  = $users{$k}->get_propername();
    my $year        = $users{$k}->get_year();
    my $yearbookQ   = $users{$k}->get_yearbookQ();
    my $yearbookA   = $users{$k}->get_yearbookA();
    my $lanyardQ    = $users{$k}->get_lanyardQ();
    my $lanyardA    = $users{$k}->get_lanyardA();
    my $pacduesQ    = $users{$k}->get_pacduesQ();
    my $pacduesA    = $users{$k}->get_pacduesA();
    my $spiritlifeQ = $users{$k}->get_spiritlifeQ();
    my $spiritlifeA = $users{$k}->get_spiritlifeA();
    my $otherQ      = $users{$k}->get_otherQ();
    my $otherA      = $users{$k}->get_otherA();
    my $cafe        = $users{$k}->get_cafe();
    my $total       = $users{$k}->get_total();

    # creating individual user receipt string

    #CR        
    #my $sr = "Student: $k\nLCHS-$lname\n$propername\n";
    my $sr = "\n\nStudent: $k\n$lname\n$propername\n";

#   $sr .= sprintf("LCHS-%-15.15s\n",$lname);
#    $sr .= sprintf("%-20.20s\n",$propername);
    #CR
    #$sr .= sprintf("%-9s-----------\n",$year);
    $sr .= sprintf("%-11s---------\n",$year);


    my $yearbookA_s = sprintf("%4.2f",$yearbookA);
    $sr .= sprintf("Yearbook(%1d)%1s\$%7s\n",$yearbookQ,' ',$yearbookA_s);

    my $lanyardA_s = sprintf("%4.2f",$lanyardA);
    $sr .= sprintf("Lanyard(%1d)%2s\$%7s\n",$lanyardQ,' ',$lanyardA_s);

    my $pacduesA_s = sprintf("%4.2f",$pacduesA);
    $sr .= sprintf("PAC(%1d)%6s\$%7s\n",$pacduesQ,' ',$pacduesA_s);

    my $spiritlifeA_s = sprintf("%4.2f",$spiritlifeA);
    $sr .= sprintf("Srv Club(%1d)%1s\$%7s\n",$spiritlifeQ,' ',$spiritlifeA_s);

    my $otherA_s = sprintf("%4.2f",$otherA);
    $sr .= sprintf("Other(%1d)%4s\$%7s\n",$otherQ,' ',$otherA_s);

    my $cafe_s = sprintf("%4.2f",$cafe);
    $sr .= sprintf("Cafeteria%3s\$%7s\n",' ',$cafe_s);

    #CR
    #my $student_recipt = "Student: $k\nLCHS-$lname\n$propername\n$year -----------\nYearbook($yearbookQ)\t\$$yearbookA\nLanyard($lanyardQ)\t\$$lanyardA\nPAC($pacduesQ)\t\t\$$pacduesA\nSpirt Life($spiritlifeQ)\t\$$spiritlifeA\nCafe\t\t\$$cafe\n--------------------\nSUBTOTAL\t\$$total\n\n";
    my $student_recipt = "Student: $k\n$lname\n$propername\n$year ---------\nYearbook($yearbookQ)\t\$$yearbookA\nLanyard($lanyardQ)\t\$$lanyardA\nPAC($pacduesQ)\t\t\$$pacduesA\nSpirt Life($spiritlifeQ)\t\$$spiritlifeA\nCafe\t\t\$$cafe\n--------------------\nSUBTOTAL\t\$$total\n\n";
    #MAR
    # add line of dashes before subtotal and fix subtotal
    $sr .= "--------------------\n";
    my $total_s = sprintf("%4.2f",$total);
    $sr .= sprintf("SUBTOTAL%4s\$%7s\n",' ',$total_s);
    # END MAR
    $receipt .= $sr; # appending individual user to main receipt
}

# -Creating Footer-
#CR
#my $receipt_footer = "\nTOTALS:\n";
my $receipt_footer = "\n\nTOTALS:\n";


keys %users; # reset the internal iterator so a prior each() doesn't affect the loop
# Getting the total of each user and adding that to a grand total
while(my($k, $v) = each %users) {
    $users{$k}->update_total(); #updating user's total
    my $total = $users{$k}->get_total(); #getting user's total
    $grand_total += $total; # adding user's total to grand total
    my $total_s = sprintf("%4.2f",$total);
    #CR
    #$receipt_footer .= sprintf("(%6d)%4s\$%7s\n",$k,' ',$total_s);
    $receipt_footer  .= sprintf("(%7d)%3s\$%7s\n",$k,' ',$total_s);
#    $receipt_footer .= "($k)\t\t\$$total\n"; # adding user subtotal to footer
}

$receipt_footer .= "--------------------\n";

my $grand_total_s = sprintf("%4.2f",$grand_total);
$receipt_footer .= sprintf("TOTAL%7s\$%7.7s\n",' ',$grand_total_s);



$receipt .= $receipt_footer; # appending footer to main receipt 
$receipt .= "\n";   

return $receipt;

    
}

#--------------------------------------------------------
# Prints a title for the beginning of the program
#--------------------------------------------------------
sub title {
    print "///////////////////////////////////////////////////////////////////////\n";
    print "////                       STARTUP DAY TOOL                        ////\n";
    print "////       LICENSED TO LEXINGTON CATHOLIC HIGH SCHOOL - 2016       ////\n";
    print "///////////////////////////////////////////////////////////////////////\n";
}

#--------------------------------------------------------
# Transaction Header
#--------------------------------------------------------
# argument: transaction number
sub transaction_header {
    my $number = shift;
    print "\n_____________________Transaction Number: $number ________________________\n";
}


#--------------------------------------------------------
# mySQL
#--------------------------------------------------------
sub GetInfo {
    #-------------------------local variables---------------------------------------------
    my $parmnumber = @_;        # number of args passed
    my ($IDNum,@arglist) = @_;  # pop off IDNUM (database key) and put everything else in a list
    my $select = "";        # field name of first argument in select is always IDNUM
    my @returnargs;         # array of values to return to calling pgm
    my $debugit = 0;        # turn debugging on/off
    my $RoutineName = "Getinfo";    # name of subroutine (for debugging)
    my $RecordCount = 0;        # number of records returned from query
    #-------------------------database connecton variables--------------------------------
    my $dbi  = "dbi";
    my $servertype = "mysql";
    my $server = "lchsweb.lexingtoncatholic.local";
    my $mydatabase = "lchsdb";  
    #my $mydatabase = "lchsdb_test";
    my $user = q/startup/;                  # user set up for the cashiers - select on people, insert on startuplog     
    my $password = q/Lch$Startup/;            # password for user above would go here - SO MAKE SURE NO ONE SEES THIS CODE!
    my $dbh = "";       # db database handle
    my $sth = "";       # db statement handle
    my $sql ="";        # sql statement
    my @row="";     # row returned from select
    #---------------------------------------------------------------------------------------
    


    if($debugit) {
        print "DEBUG $RoutineName: number of args passed: $parmnumber \n";
        print "DEBUG $RoutineName: @arglist\n";
    }

    #------------------------------------------------------------------ 
    # go through the list of field names passed in arglist and build a
    # comma delimited list of fields to use in a SQL Select 
    #------------------------------------------------------------------
    foreach (@arglist) {    # build the select stmt from the field desired
        $select = $select.$_.",";
        if($debugit) {
            print "DEBUG $RoutineName: field to get info for:  $_ \n";
        }
        
    }
    chop($select);   # remove last comma in the list
    if($debugit) {
        print "DEBUG $RoutineName: select is $select \n";  # Select options
    }
    
    #--------------------------------------------------------------------------------
    # build the SQL statment to get the information requested in arglist
    #--------------------------------------------------------------------------------
    $sql = "SELECT $select FROM People WHERE IDNum=? AND Status = \"Active\"";
    if($debugit) {
        print "DEBUG $RoutineName: $sql \n";
    }

    
    #-----------------------------------------------------------------------
    # connect, prepare, and execute select statement - mysql - lchsweb
    #-----------------------------------------------------------------------                                   
    $dbh = DBI->connect("$dbi:$servertype:database=$mydatabase:host=$server",$user,$password)
        or die "Can't connect to  $DBI::errstr";
    if($debugit) {
        print "DEBUG $RoutineName: database $mydatabase connconnected successfully \n";
    }
    $sth = $dbh->prepare($sql) 
        or die "Can't prepare statement: $DBI::errstr";
    $sth->execute($_[0]) 
        or die "Could not execute SQL Statement $DBI::errstr";
    if($debugit) {
        print "DEBUG $RoutineName: prepare and execute successful for id $_[0] \n";
    }

    #---------------------------------------------------------
    # process and count the rows returned in the select 
    # there should only be one - anything else is a problem
    #---------------------------------------------------------
    while (@row = $sth->fetchrow_array) {
        if($debugit) {
            print "DEBUG $RoutineName: loaded record in fetch array @row \n";
        }
        @returnargs = @row; # load the return array now.  @row will be null once if fetchrow is empty
        $RecordCount++;
    }

    if($debugit == 1) {
        print "DEBUG $RoutineName: record count is $RecordCount \n";
        print "DEBUG $RoutineName: row array is @row  at end of fetch\n";
        print "DEBUG $RoutineName: return array is @returnargs at end of fetch\n"   
    }

    #---------------------------------------------------------------------
    # Look for errors and tell if something is wrong;
    #---------------------------------------------------------------------
    if($RecordCount == 1) {     # good
        # do nothing - the values to return have already been loaded.
    } elsif ($RecordCount == 0) {   # student id not in database
        print "DATABASE WARNING:  student ID  $_[0] is not found in database \n";
        print "Skipping $_[0] \n";
    } elsif ($RecordCount >  1) {   # multiple records returned so stop
        print "DATABASE ERROR: multiple SQL records ( $RecordCount ) found for $_[0] \n";
        print "Skipping $_[0] \n";
    } elsif ($RecordCount < 0 ) {   # sql problem?   so stop
        print "FATAL PGM ERROR: this should never happen ( $RecordCount ) found for $_[0]\n";
        die;
    }
    

    #-----------------------------------------------------  
    # close the handles (and files)  and exit
    #-----------------------------------------------------
    $sth->finish;
    $dbh->disconnect;

    if($debugit) {
        print "DEBUG $RoutineName: everything is closed - get out of here\n";
    }
    
    # return the values
    return ($RecordCount,@returnargs);
}

#--------------------------------------------------------
# Print Function for DYMO
#--------------------------------------------------------
sub PrintDYMO  {

    my $printline = @_[0];   # pick up the print line
    #print "PRINTLINE: $printline \n";
    
    
    #-----------------------------------------------------------------------------------------------
    # VARs - shouldn't have to tweak
    #------------------------------------------------------------------------------------------------
    use Sys::Hostname; #used for printing
    my $printername = "DYMO";  # change only if the DYMO printer isn't name "DYMO"
    my $mySRV = hostname;   # laptop's name
    my $lp = "";
    my $jobkey = "";
    my $dateit = "";    # date and time stamp of program run
    
    my $lname  = "";    # student last name
    my $pname  = "";    # student proper (first) name
    my $grade  = "";    # grade in "ClassOf" format
    my $studentid = ""; # student id number from bar code
    my $cashier = "";   # cashier's initials used as part of the transacion id (2 chars)
    my $TransactionID = ""; # unique number to identify this transaction receipt
    print "Using print server $mySRV \n";

    # this section sets up all the pointers needed for printing
    $lp = new Net::LPR(
        StrictRFCPorts => 0,
        RemoteServer => "$mySRV",
        RemotePort => 515,
        PrintErrors => 0,
        RaiseErrors => 1,
    );
    $lp->connect();
    print "connect successful\n";

    $jobkey = $lp->new_job();
    print "jobkey set\n";

    $lp->send_jobs("$printername");
    print "send job ok \n";

    $lp->job_mode_text($jobkey);
    print "job mode text ok \n";

    $lp->job_send_control_file($jobkey);
    print "job send control file ok\n";
    
    # this actually does the printing
    $lp->job_send_data($jobkey, $printline, length($printline));

    $lp->disconnect;
    
    #-----------
    print "Hit any key or scan to print second receipt";
    <STDIN>;
    #-----------
    $lp = new Net::LPR(
        StrictRFCPorts => 0,
        RemoteServer => "$mySRV",
        RemotePort => 515,
        PrintErrors => 0,
        RaiseErrors => 1,
    );

    $lp->connect();
    print "connect successful\n";
    $jobkey = $lp->new_job();
    print "jobkey set\n";

    $lp->send_jobs("$printername");
    print "send job ok \n";

    $lp->job_mode_text($jobkey);
    print "job mode text ok \n";

    $lp->job_send_control_file($jobkey);
    print "job send control file ok\n";
    
    # this actually does the printing
    $lp->job_send_data($jobkey, $printline, length($printline));
    
    
    $lp->disconnect;
        
    return;
}






















#==========================================================================================
# Main Program
#==========================================================================================
clear_screen(); #clearing cmd line screen
title(); # printing title to screen


# declare global variables
our $attendant = " ";

# declare local variables
my $input = " ";

print color($AskColor),"Starting main program \n",color("reset");
print color("$AskColor"),"Enter your initials: ",color("reset");
$input = <STDIN>;
$attendant = uc (substr $input,0,2);


# Logic to control main program loop
do {
  Transaction();
  print "\nPress Enter for a new transaction or quit to end \n";
  $input = <STDIN>;
  clear_screen();
   
} until ($input eq "quit\n");

print "Exiting main program\n";

# Add call to close connection to MySQL database

exit;


# Main Transaction Routine
sub Transaction {

#--------------------------------------------------------
# Variable Initialization
#--------------------------------------------------------
# Inventory Items/Price
my $yearbook = "YEARBOOK";
my $yearbook_price = 100;

my $lanyard  = "LANYARD";
my $lanyard_price = 5;

#CR
my $spiritlife = "SERVICE CLUB";
my $spiritlife_price = 20;

my $other = "OTHER";
my $other_price = 10;

#CR
my $pacdues = "PAC DUES";
my $pacdues_price = 35;

my $cafe = "CAFETERIA";


# Grade Levels
my $freshman = "ClassOf2020";
my $sophomore = "ClassOf2019";
my $junior = "ClassOf2018";
my $senior = "ClassOf2017";


# Required fields for storing Perosn objects
my %users = (); # hash with user id as key and reference to the id object as the value
my @keys = keys %users;
my $size = @keys; 


# Required fields for mySQL person
my $rc = 0; #return code from mysql function
my $fname = "NULL";
my $lname = "NULL";
my $propername = "NULL";
my $gradelevel = "NULL";
my $enrollyear = "NULL";



# Other
# my $attendant = "SR"; # initials of operator of specific kiosk...used in the creation of transaction number


my $creditcard = "CARD";
my $transaction_number = our $attendant."-".midnight_seconds(); # unique number based off of seconds since midnight
my $payment_method = "NULL"; # initializing payment method
my $check_number = 0; # initializing check number
my $cc_type = "NULL"; # initializing credit card type
my $grand_total = 0; # initializing grand total for transaction
my $current_year = 2016;


# Used to determine whether an input is a number
use Scalar::Util qw(looks_like_number); #looks_like_number()


#--------------------------------------------------------
# Collecting Student ID and verifying against mySQL
#--------------------------------------------------------
# Getting ID from user
my $message = "Please SCAN Student Number: ";
my $input = get_input($message);
if (!looks_like_number($input)) {
   print "=== $input is not a number, transaction cancelled\n";
   return;
}

#--------------------------------------------------------
# Creating new user if mySQl is verified and adding object to 'user' hash
#--------------------------------------------------------
my $current_user = $input;
($rc,$fname, $lname, $propername, $gradelevel, $enrollyear) = GetInfo($current_user,"Fname","Lname","pname","GradClass","EnrollYear");

if ($rc == 1){
    my $new_object = new Person($current_user,$fname,$lname,$propername,$gradelevel,$enrollyear);
    $users{$current_user} = $new_object;
}
else{
    print "=== $input was not found in the database, transaction cancelled\n";
    print "return code $rc";
    return;
}



#--------------------------------------------------------
# Transaction header
#--------------------------------------------------------
transaction_header($transaction_number);


#--------------------------------------------------------
# Adding item to the inventory/creating a new user if necessary
#--------------------------------------------------------
# loop runs until user enters specified character to quit
while ($input ne 'PRINT'){
    my $price = 0; #initializing price

    # Getting User Input
    $message = "Please SCAN Next Item or Student Number or enter Action (TOTAl,PRINT,NEWTRANSACTION): ";
    my $input = get_input($message);
    
    #--------------------------------------------------------
    # Branching depending on what user entered
    #--------------------------------------------------------
    # - User entered a number (assumed to be a student id)
    if (looks_like_number($input)) {
        # ... NEED TO CHECK AGAINST MYSQL
        $current_user = $input; #setting current user
        print "\n>>Current student switched to: $current_user\n"; #output to screen

        # Determine if the specified user already exists, or if a new one needs to be created
        if (exists($users{$current_user})){
            print "user already exists\n\n";
        }
        else {
            # Creating new user and adding to 'user' hash
            $current_user = $input;
            ($rc,$fname, $lname, $propername, $gradelevel, $enrollyear) = GetInfo($current_user,"Fname","Lname","pname","GradClass","EnrollYear");
            if ($rc == 1){
                my $new_object = new Person($current_user,$fname,$lname,$propername,$gradelevel,$enrollyear);
                $users{$current_user} = $new_object;
            }
            else{
                die('--error-- GetInfo function failed with code $rc');
            }
            print "new user created\n\n";
            
        } 
    }
    # - User entered a char deemed to be a signal to finish the transaction
    elsif ($input eq 'PRINT'){
        last; #breaking out of loop because user indicated they wanted to finish the transaction
    }
    # - User entered char deemed to be a signal to cancel this transaction
    elsif ($input eq 'NEWTRANSACTION') {
         print "==Transaction Cancelled==\n";
         return;
    }
    # - User entered a char deemed to be a signal to display a current total of the transaction
    elsif ($input eq 'TOTAL'){
        clear_screen();
        print show_totals(%users);
    }
    # - User entered a char string (assumed to be an inventory item)
    else {
        # ---Yearbook---
        if ($input eq $yearbook){
            $price = $yearbook_price;
            # Checking rule for senior regarding yearbook (senior yearbook is free)
            if ($users{$current_user}->get_year() eq $senior && $users{$current_user}->get_yearbookQ() == 0){
                print "\n==WARNING== senior yearbook is free";
                $price = 0;
            }
            # Making sure only 1 yearbook can be purchased per user
            if ($users{$current_user}->get_yearbookQ() > 0){
                print "\n==WARNING== only 1 yearbook can be purchased per student.\n\n";
                $input = "---";
                $price = "---";
            }
            # Adding yearbook to transaction
            else {
                $users{$current_user}->set_yearbookQ($users{$current_user}->get_yearbookQ() + 1); #incrementing quantity
                $users{$current_user}->set_yearbookA($users{$current_user}->get_yearbookA() + $price) #adding price to total amount 
            }
        }
        # ---Lanyard---
        elsif ($input eq $lanyard){
            print "\n==WARNING== remember to give student lanyard";
            $price = $lanyard_price; #setting price

            # First lanyard is free for freshman and incoming students
            if ((($users{$current_user}->get_enrollyear() - $current_year) eq 0) && $users{$current_user}->get_lanyardQ == 0){
                print "\n==WARNING== only the first lanyard is free for freshmen and incoming students\n";
                $price = 0;
            }

            # Adding lanyard to transaction
            $users{$current_user}->set_lanyardQ($users{$current_user}->get_lanyardQ() + 1); #incrementing quantity
            $users{$current_user}->set_lanyardA($users{$current_user}->get_lanyardA() + $price) #adding price to total amount
        }
        # --- Spiritual Life ---
        elsif ($input eq $spiritlife){
            $price = $spiritlife_price; #setting price

            # Adding Spiritual Life to transaction
            $users{$current_user}->set_spiritlifeQ($users{$current_user}->get_spiritlifeQ() + 1); #incrementing quantity
            $users{$current_user}->set_spiritlifeA($users{$current_user}->get_spiritlifeA() + $price) #adding price to total amount
        }
        # --- Other ---
        elsif ($input eq $other){
            $price = $other_price; #setting price

            # Adding other to transaction 
            $users{$current_user}->set_otherQ($users{$current_user}->get_otherQ() + 1); #incrementing quantity
            $users{$current_user}->set_otherA($users{$current_user}->get_otherA() + $price) #adding price to total amount
        }
        # --- PAC Dues ---
        elsif ($input eq $pacdues){
            $price = $pacdues_price; #setting price

            # Adding PAC dues to transaction
            $users{$current_user}->set_pacduesQ($users{$current_user}->get_pacduesQ() + 1); #incrementing quantity
            $users{$current_user}->set_pacduesA($users{$current_user}->get_pacduesA() + $price) #adding price to total amount
        }
        # --- Cafeteria ---
        elsif ($input eq $cafe){
            $message = "\nEnter amount to be paid: ";
            $price = get_input($message); #setting price
                 if (!looks_like_number($price)) {
                   print "Invalid amount ($price) entered, zero assumed\n";
                   $price = 0;
                   }

            # Adding amount to transaction
            $users{$current_user}->set_cafe($users{$current_user}->get_cafe() + $price); #setting total of object
        }
        # Reaching this point means the input is not valid
        else {
            print "\n==WARNING== Invalid Item Scanned:'$input'\n";
            $input = "---";
            $price = "---";
        }

        # Printing scanned item to screen
        my $fnamelname = $users{$current_user}->get_fname()." ".$users{$current_user}->get_lname(); #creating full name based on fname and lname
        if ($price ne "---") {
          print "\nitem added to ($fnamelname) >> $input\t\$$price\n\n";
        }
    } 
}


#--------------------------------------------------------
# Debugging 
#--------------------------------------------------------
use Data::Dumper;
#print Dumper(\%users);


#--------------------------------------------------------
# Debugging
#--------------------------------------------------------
#keys %users; # reset the internal iterator so a prior each() doesn't affect the loop
#while(my($k, $v) = each %users) {
#    $users{$k}->update_total(); 
#    my $subtotal = $users{$k}->get_total();
#    print "key: $k, total: $subtotal\n";
#}


# BEGIN MARK RITCHIE CODE------------------------------------------------------------
#--------------------------------------------------------
# Determining payment method
#--------------------------------------------------------
my $pay_forms = "CASH CHECK CARD";
my $rc1 = -1;
$message = "Please SCAN payment method: ";
clear_screen();
print "\n\n==ATTENTION!== a 3% fee will be added to all card payments\n";
do {

    $payment_method = get_input($message);

    #CR
    if($payment_method eq "CREDIT CARD") {
	$payment_method = "CARD";
    }

    $rc1 = index($pay_forms,$payment_method);
    } until ($rc1 >= 0);


if ($payment_method eq "CARD") {
    print "paying with card\n";
    $payment_method = "CARD";
}
elsif ($payment_method eq "CHECK") {
    $payment_method = "CHECK: ";
    $message = "Please enter the the check number: ";
    $check_number = get_input($message);
    $payment_method .= $check_number;
}
else {
    print "paying with cash\n";
    $payment_method = "CASH";
}


#--------------------------------------------------------
# Creating Receipt
#--------------------------------------------------------
# -Creating Header-
use POSIX qw(strftime);
my $receipt = "";

#CR
#my $datestring = strftime '%x %X',localtime(); # getting date and time
my $datestring = substr(localtime(),4);


my $receipt_header = "--LCHS STARTUP DAY--\n$datestring\n\n";
$receipt .= $receipt_header; # appending header to main receipt

# -Creating Body-
# Looping through all users getting necessary information for receipt
keys %users; # reset the internal iterator so a prior each() doesn't affect the loop
while(my($k, $v) = each %users) {
    $users{$k}->update_total(); # making sure totals are up to date

    # Retrieving a user's information
    my $lname       = $users{$k}->get_lname();
    my $propername  = $users{$k}->get_propername();
    my $year        = $users{$k}->get_year();
    my $yearbookQ   = $users{$k}->get_yearbookQ();
    my $yearbookA   = $users{$k}->get_yearbookA();
    my $lanyardQ    = $users{$k}->get_lanyardQ();
    my $lanyardA    = $users{$k}->get_lanyardA();
    my $pacduesQ    = $users{$k}->get_pacduesQ();
    my $pacduesA    = $users{$k}->get_pacduesA();
    my $spiritlifeQ = $users{$k}->get_spiritlifeQ();
    my $spiritlifeA = $users{$k}->get_spiritlifeA();
    my $otherQ      = $users{$k}->get_otherQ();
    my $otherA      = $users{$k}->get_otherA();
    my $cafe        = $users{$k}->get_cafe();
    my $total       = $users{$k}->get_total();

    # creating individual user receipt string

    #CR        
    #my $sr = "Student: $k\nLCHS-$lname\n$propername\n";
    my $sr = "\n\nStudent: $k\n$lname\n$propername\n";

#   $sr .= sprintf("LCHS-%-15.15s\n",$lname);
#    $sr .= sprintf("%-20.20s\n",$propername);
    #CR
    #$sr .= sprintf("%-9s-----------\n",$year);
    $sr .= sprintf("%-11s---------\n",$year);


    my $yearbookA_s = sprintf("%4.2f",$yearbookA);
    $sr .= sprintf("Yearbook(%1d)%1s\$%7s\n",$yearbookQ,' ',$yearbookA_s);

    my $lanyardA_s = sprintf("%4.2f",$lanyardA);
    $sr .= sprintf("Lanyard(%1d)%2s\$%7s\n",$lanyardQ,' ',$lanyardA_s);

    my $pacduesA_s = sprintf("%4.2f",$pacduesA);
    $sr .= sprintf("PAC(%1d)%6s\$%7s\n",$pacduesQ,' ',$pacduesA_s);

    my $spiritlifeA_s = sprintf("%4.2f",$spiritlifeA);
    $sr .= sprintf("Srv Club(%1d)%1s\$%7s\n",$spiritlifeQ,' ',$spiritlifeA_s);

    my $otherA_s = sprintf("%4.2f",$otherA);
    $sr .= sprintf("Other(%1d)%4s\$%7s\n",$otherQ,' ',$otherA_s);

    my $cafe_s = sprintf("%4.2f",$cafe);
    $sr .= sprintf("Cafeteria%3s\$%7s\n",' ',$cafe_s);

    #CR
    #my $student_recipt = "Student: $k\nLCHS-$lname\n$propername\n$year -----------\nYearbook($yearbookQ)\t\$$yearbookA\nLanyard($lanyardQ)\t\$$lanyardA\nPAC($pacduesQ)\t\t\$$pacduesA\nSpirt Life($spiritlifeQ)\t\$$spiritlifeA\nCafe\t\t\$$cafe\n--------------------\nSUBTOTAL\t\$$total\n\n";
    my $student_recipt = "Student: $k\n$lname\n$propername\n$year ---------\nYearbook($yearbookQ)\t\$$yearbookA\nLanyard($lanyardQ)\t\$$lanyardA\nPAC($pacduesQ)\t\t\$$pacduesA\nSpirt Life($spiritlifeQ)\t\$$spiritlifeA\nCafe\t\t\$$cafe\n--------------------\nSUBTOTAL\t\$$total\n\n";
    #MAR
    # add line of dashes before subtotal and fix subtotal
    $sr .= "--------------------\n";
    my $total_s = sprintf("%4.2f",$total);
    $sr .= sprintf("SUBTOTAL%4s\$%7s\n",' ',$total_s);
    # END MAR
    $receipt .= $sr; # appending individual user to main receipt
}

# -Creating Footer-
#CR
#my $receipt_footer = "\nTOTALS:\n";
my $receipt_footer = "\n\nTOTALS:\n";


keys %users; # reset the internal iterator so a prior each() doesn't affect the loop
# Getting the total of each user and adding that to a grand total
while(my($k, $v) = each %users) {
    $users{$k}->update_total(); #updating user's total
    my $total = $users{$k}->get_total(); #getting user's total
    $grand_total += $total; # adding user's total to grand total
    my $total_s = sprintf("%4.2f",$total);
    #CR
    #$receipt_footer .= sprintf("(%6d)%4s\$%7s\n",$k,' ',$total_s);
    $receipt_footer  .= sprintf("(%7d)%3s\$%7s\n",$k,' ',$total_s);
#    $receipt_footer .= "($k)\t\t\$$total\n"; # adding user subtotal to footer
}

$receipt_footer .= "--------------------\n";
# Adding 3% for credit card transactions

if ($payment_method eq $creditcard) {
        my $cc_charge= $grand_total * 0.03;
        my $cc_charge_s = sprintf("%3.2f",$cc_charge);
        $grand_total += $cc_charge;
        $receipt_footer .= sprintf("CC CHARGE%4s\$%6s\n",' ',$cc_charge_s);
}
my $grand_total_s = sprintf("%4.2f",$grand_total);
$receipt_footer .= sprintf("TOTAL%7s\$%7.7s\n",' ',$grand_total_s);
$receipt_footer .= "\n\nPayment-$payment_method\n";


$receipt .= $receipt_footer; # appending footer to main receipt
# END MARK RITCHIE CODE------------------------------------------------------------


#--------------------------------------------------------
# Writing receipt to Log file
#--------------------------------------------------------
store_receipt ($transaction_number,$receipt);


#--------------------------------------------------------
# Printing Receipt
#--------------------------------------------------------
clear_screen();
print $receipt;
&PrintDYMO($receipt); #printing receipt



print "\n";
print "end of transaction...\n";
print "------------------------------------------------\n";
}



