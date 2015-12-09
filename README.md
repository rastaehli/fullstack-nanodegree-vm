fullstack-nanodegree-vm
=============

Forked from the Udacity fullstack-nanodegree-vm repository, this project contains my solution for storing Tournament results in a Postgres database and computing  “Swiss Pairings” for each round of matches.

The current functionality is demonstrated by running the python code in tournament_test.py.  Here’s how:

- clone this project to your machine and change to the vagrant directory:
<pre>
    cd /vagrant
</pre>
- launch the virtual machine and enter a virtual terminal:
<pre>    
    vagrant up
    vagrant ssh
</pre>
- in the VM, cd to the tournament folder and initialize the database:
<pre>    
    cd /vagrant/tournament
    psql
    \i tournament.sql
    \q
</pre>
- run the unit tests and verify it reports success:
<pre>    
    python tournament_test.py
</pre>

