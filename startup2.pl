#!/usr/local/bin/perl
use warnings; #looks_like_number()
use strict;
use Data::Dumper;




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
	chomp(my $userInput = <>);

	return $userInput;
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

    open(my $fh, '>', 'Logs/'.$filename.'.txt') or die("error:\topening file\n");
    print $fh "$data";
    close $fh;
}

sub show_totals {
    my (%users) = @_;
    my $grand_total = 0;
    

    # -Creating Header-
    my $receipt = "";
    my $datestring = localtime();
    my $receipt_header = "--LCHS STARTUP DAY--\n$datestring\n\n";
    $receipt .= $receipt_header;

    # -Creating Body-
    # Looping through all students getting necessary information for receipt
    keys %users; # reset the internal iterator so a prior each() doesn't affect the loop
    while(my($k, $v) = each %users) {
        $users{$k}->update_total();

        my $lname = $users{$k}->get_lname();
        my $propername = $users{$k}->get_propername();
        my $year = $users{$k}->get_year();
        my $yearbookQ = $users{$k}->get_yearbookQ();
        my $yearbookA = $users{$k}->get_yearbookA();
        my $lanyardQ = $users{$k}->get_lanyardQ();
        my $lanyardA = $users{$k}->get_lanyardA();
        my $pacduesQ = $users{$k}->get_pacduesQ();
        my $pacduesA = $users{$k}->get_pacduesA();
        my $spiritlifeQ = $users{$k}->get_spiritlifeQ();
        my $spiritlifeA = $users{$k}->get_spiritlifeA();
        my $cafe = $users{$k}->get_cafe();
        my $total = $users{$k}->get_total();

        my $student_recipt = "Student: $k\nLCHS-$lname\n$propername\n$year -----------\nYearbook($yearbookQ)\t\$$yearbookA\nLanyard($lanyardQ)\t\$$lanyardA\nPAC($pacduesQ)\t\t\$$pacduesA\nSpirt Life($spiritlifeQ)\t\$$spiritlifeA\nCafe\t\t\$$cafe\n--------------------\nSUBTOTAL\t\$$total\n\n";
        $receipt .= $student_recipt;  
    }

    # -Creating Footer-
    my $receipt_footer = "\nTOTALS:\n";
    keys %users; # reset the internal iterator so a prior each() doesn't affect the loop
    while(my($k, $v) = each %users) {
        $users{$k}->update_total(); #updating user's total
        my $total = $users{$k}->get_total(); #getting user's total
        $grand_total += $total;

        $receipt_footer .= "($k)\t\t\$$total\n"; # adding user subtotal to footer
    }
    $receipt_footer .= "--------------------\nTOTAL\t\t\$$grand_total\n\n\n\n"; #adding grand total to footer
    $receipt .= $receipt_footer; # finalizing receipt
    
    

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























#==========================================================================================
# Main Program
#==========================================================================================
clear_screen(); #clearing cmd line screen
title(); # printing title to screen


#--------------------------------------------------------
# Variable Initialization
#--------------------------------------------------------
# Inventory Items/Price
my $yearbook = "YEARBOOK";
my $yearbook_price = 10;

my $lanyard  = "LANYARD";
my $lanyard_price = 10;

my $spiritlife = "SPRTLIFE";
my $spiritlife_price = 10;

my $other = "OTHER";
my $other_price = 10;

my $pacdues = "PAC";
my $pacdues_price = 10;

my $cafe = "CAFETERIA";


# Grade Levels
my $freshman = "freshman";
my $sophomore = "sophomore";
my $junior = "junior";
my $senior = "senior";


# Required User Fields...should be getting filled with mySQL
my %users = (); # hash with user id as key and reference to the id object as the value
my @keys = keys %users;
my $size = @keys; 

my $fname = "Stephen";
my $lname = "Ritchie";
my $propername = "Stephen Ritchie";
my $gradelevel = $freshman;


# Other
my $attendant = "SR"; # initials of operator of specific kiosk...used in the creation of transaction numbermy $creditcard = "CARD";
my $transaction_number = $attendant."-".midnight_seconds(); # unique number based off of seconds since midnight
my $payment_method = "NULL"; # initializing payment method
my $check_number = 0; # initializing check number
my $cc_type = "NULL"; # initializing credit card type
my $grand_total = 0; # initializing grand total for transaction
my $creditcard = "card";



#--------------------------------------------------------
# Collecting Student ID and verifying against mySQL
#--------------------------------------------------------
# Getting ID from user
my $message = "Please SCAN Student Number: ";
my $input = get_input($message);

# Checking ID against mySQl database
if (!mysql_check($input)) {
    $input = get_input($message);
    if (!mysql_check($input)) {
        die ("The ID entered is not in the Startup Database, stopped"); #exiting program if two consectuive invalid IDs have been entered
    }
}


#--------------------------------------------------------
# Creating new user if mySQl is verified and adding object to 'user' hash
#--------------------------------------------------------
my $current_user = $input;
my $new_object = new Person($current_user,$fname,$lname,$propername,$gradelevel);
$users{$current_user} = $new_object;


#--------------------------------------------------------
# Creating transaction header
#--------------------------------------------------------
transaction_header($transaction_number);


#--------------------------------------------------------
# Adding item to the inventory/creating a new user if necessary
#--------------------------------------------------------
use Scalar::Util qw(looks_like_number); #looks_like_number()
# loop runs until user enters specified character to quit
while ($input ne 'f'){
	my $price = 0; #initializing price

	# Getting User Input
    $message = "Please SCAN Next Item or Student Number: ";
    my $input = get_input($message);
    
    # Branching depending on what user entered
    # -User enterd a number (assumed to be a student id)
    if (looks_like_number($input)) {
    	# ... NEED TO CHECK AGAINST MYSQL
        $current_user = $input; #setting current user
        print "\n>>Current student switched to: $current_user\n"; #output to screen

        # Determing if the specified user already exists, or if a new one needs to be created
        if (exists($users{$current_user})){
        	print "user already exists\n\n";
        }
        else {
        	print "new user created\n\n";
        	# Creating new user and adding to 'user' hash
        	$current_user = $input;
            # ... GET INFO FROM MYSQL
        	$new_object = new Person($current_user,$fname,$lname,$propername,$gradelevel);
        	$users{$current_user} = $new_object;
        } 
    }
    # -User entered a char deemed to be a signal to finish the transaction
    elsif ($input eq 'f'){
        last; #breaking out of loop becasue user indicated they wanted to finish the transaction
    }
    # -User entered a char deemed to be a signal to display a current total of the transaction
    elsif ($input eq 't'){
        clear_screen();
        print show_totals(%users);
    }
    # -User entered a char string (assumed to be an inventory item)
    else {
        # ---Yearbook---
    	if ($input eq $yearbook){
    		$price = $yearbook_price;
    		# Checking rule for senior regarding yearbook (senior yearbook is free)
    		if ($gradelevel eq $senior && $users{$current_user}->get_yearbookQ() == 0){
    			print "\n==WARNING== senior yearbook is free...sort of";
    			$price = 0;
    		}
            # Making sure only 1 yearbook can be purchased per user
    		if ($users{$current_user}->get_yearbookQ() > 0){
    			print "\n==WARNING== only 1 yearbook can be purchased per student.";
    			$input = "---";
    		    $price = "---";
    		}
    		else {
    			$users{$current_user}->set_yearbookQ($users{$current_user}->get_yearbookQ() + 1); #incrementing quantity
    			$users{$current_user}->set_yearbookA($users{$current_user}->get_yearbookA() + $price) #adding price to total amount	
    		}
    	}
        # ---Lanyard---
    	elsif ($input eq $lanyard){
    		print "\n==WARNING== remember to give student lanyard";
    		$price = $lanyard_price;
    		$users{$current_user}->set_lanyardQ($users{$current_user}->get_lanyardQ() + 1); #incrementing quantity
    		$users{$current_user}->set_lanyardA($users{$current_user}->get_lanyardA() + $price) #adding price to total amount
    	}
        # --- Spiritual Life ---
    	elsif ($input eq $spiritlife){
    		$price = $spiritlife_price;
    		$users{$current_user}->set_spiritlifeQ($users{$current_user}->get_spiritlifeQ() + 1); #incrementing quantity
            $users{$current_user}->set_spiritlifeA($users{$current_user}->get_spiritlifeA() + $price) #adding price to total amount
    	}
        # --- Other ---
        elsif ($input eq $other){
            $price = $other_price;
            $users{$current_user}->set_otherQ($users{$current_user}->get_otherQ() + 1); #incrementing quantity
            $users{$current_user}->set_otherA($users{$current_user}->get_otherA() + $price) #adding price to total amount
        }
        # --- PAC Dues ---
    	elsif ($input eq $pacdues){
    		$price = $pacdues_price;
    		$users{$current_user}->set_pacduesQ($users{$current_user}->get_pacduesQ() + 1); #incrementing quantity
            $users{$current_user}->set_pacduesA($users{$current_user}->get_pacduesA() + $price) #adding price to total amount
    	}
        # --- Cafeteria ---
    	elsif ($input eq $cafe){
    		$message = "\nEnter amount to be paid: ";
    		$price = get_input($message); #setting price
    		$users{$current_user}->set_cafe($users{$current_user}->get_cafe() + $price); #setting total of object
    	}
    	else {
    		print "\n==WARNING== Invalid Item Scanned";
    		$input = "---";
    		$price = "---";
    	}

        # Printing scanned item to screen
        my $fnamelname = $users{$current_user}->get_fname()." ".$users{$current_user}->get_lname(); #creating full name based on fname and lname
        print "\nitem added to ($fnamelname) >> $input\t\$$price\n\n";
    } 
}


#--------------------------------------------------------
# Debugging 
#--------------------------------------------------------
use Data::Dumper;
print Dumper(\%users);


#--------------------------------------------------------
# Debugging
#--------------------------------------------------------
keys %users; # reset the internal iterator so a prior each() doesn't affect the loop
while(my($k, $v) = each %users) {
    $users{$k}->update_total(); 
    my $subtotal = $users{$k}->get_total();
    print "key: $k, total: $subtotal\n";
}


#--------------------------------------------------------
# Determing payment method
#--------------------------------------------------------
$message = "Please SCAN payment method: ";
print "==ATTENTION!== a 3% fee will be added to all card payments\n";
$payment_method = get_input($message);

if ($payment_method eq "cash") {
    print "paying in cash\n";
    $payment_method = "CASH";
}
elsif ($payment_method eq "check") {
    $payment_method = "CHECK: ";
    $message = "Please enter the the check number: ";
    $check_number = get_input($message);
    $payment_method .= $check_number;
}
else {
    print "paying in card\n";
    $payment_method = "CARD";
}


#--------------------------------------------------------
# Creating Receipt
#--------------------------------------------------------
# -Creating Header-
my $receipt = "";
my $datestring = localtime(); # getting date and time
my $receipt_header = "--LCHS STARTUP DAY--\n$datestring\n\n";
$receipt .= $receipt_header; # appending header to main receipt

# -Creating Body-
# Looping through all users getting necessary information for receipt
keys %users; # reset the internal iterator so a prior each() doesn't affect the loop
while(my($k, $v) = each %users) {
    $users{$k}->update_total(); # making sure totals are up to date

    # Retrieving a user's information
    my $lname = $users{$k}->get_lname();
    my $propername = $users{$k}->get_propername();
    my $year = $users{$k}->get_year();
    my $yearbookQ = $users{$k}->get_yearbookQ();
    my $yearbookA = $users{$k}->get_yearbookA();
    my $lanyardQ = $users{$k}->get_lanyardQ();
    my $lanyardA = $users{$k}->get_lanyardA();
    my $pacduesQ = $users{$k}->get_pacduesQ();
    my $pacduesA = $users{$k}->get_pacduesA();
    my $spiritlifeQ = $users{$k}->get_spiritlifeQ();
    my $spiritlifeA = $users{$k}->get_spiritlifeA();
    my $cafe = $users{$k}->get_cafe();
    my $total = $users{$k}->get_total();

    # creating individual user receipt string
    my $student_recipt = "Student: $k\nLCHS-$lname\n$propername\n$year -----------\nYearbook($yearbookQ)\t\$$yearbookA\nLanyard($lanyardQ)\t\$$lanyardA\nPAC($pacduesQ)\t\t\$$pacduesA\nSpirt Life($spiritlifeQ)\t\$$spiritlifeA\nCafe\t\t\$$cafe\n--------------------\nSUBTOTAL\t\$$total\n\n";
    $receipt .= $student_recipt; # appending individual user to main receipt
}

# -Creating Footer-
my $receipt_footer = "\nTOTALS:\n";
keys %users; # reset the internal iterator so a prior each() doesn't affect the loop
# Getting the total of each user and adding that to a grand total
while(my($k, $v) = each %users) {
    $users{$k}->update_total(); #updating user's total
    my $total = $users{$k}->get_total(); #getting user's total
    $grand_total += $total; # adding user's total to grand total
    $receipt_footer .= "($k)\t\t\$$total\n"; # adding user subtotal to footer
}
# Adding 3% for credit card transactions
if ($payment_method eq $creditcard) {
        my $cc_charge= $grand_total * 0.03;
        $grand_total += $cc_charge;
        $receipt_footer .= "--------------------\nCC CHARGE\t\$$cc_charge\nTOTAL\t\t\$$grand_total\n\n\nPayment-$payment_method\n"; #adding grand total to footer
}
else {
    $receipt_footer .= "--------------------\nTOTAL\t\t\$$grand_total\n\n\nPayment-$payment_method\n"; #adding grand total to footer
}

$receipt .= $receipt_footer; # appending footer to main receipt


#--------------------------------------------------------
# Writing receipt to Log file
#--------------------------------------------------------
store_receipt ($transaction_number,$receipt);


#--------------------------------------------------------
# Printing Receipt
#--------------------------------------------------------
# ... PRINT FUNCTION HERE
clear_screen();
print $receipt;
# ... sending receipt to print function







print "\n\n\n";
print "program exiting...\n";