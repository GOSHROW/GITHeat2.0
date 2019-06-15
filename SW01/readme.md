<h2>SW-01</h2>
<ul>
<li/>In order to fully access the user info, the contest list for upcoming contests, and to email a reminder, copy the given SW-01 folder to a local path.
  <li/>Thereby ensure to install the packages: <em>requests</em>, <em>smptlib</em>, <em>ssl</em> <em>datetime</em>, <em>date</em>, <em>time</em> as in
<code>pip install requests</code> in a directory accesible by python source code of local SW-01.
<li/>In order to run the files: <strong>userinf.py</strong>, <strong>contstinf.py</strong> or <strong>codeforces_email</strong>, either go for command line instructions on the terminal, 
<code>python userinf.py</code>, <code>python contstinf.py</code> <code>python codeforces_email.py</code> or run as per the local python navigator
<li/>Comply with the code's requirements as needed
<li/>Here <strong>userinf.py</strong>, <strong>contstinf.py</strong> respectively contain the code required to get the User Info of Codeforces User Handles, and to get the Contest List for Upcoming Codeforces Contests.
<li/><i>Active Internet Connection is required to contact Codeforces API, and also to send email.</i>
</ul>

<h4> CODEFORCES_EMAIL</h4>
<ul>
  <li/><strong>codeforces_email.py</strong> is used to send an e_mail reminder as per the user.
  <li/>It basically inputs the GMail id and the password of the e_mail id, after setting up an Google domain SMTP server using <i>smptlib</i>, <i>ssl</i>.
  <li/> Thereafter it would access the Start Time for any compettions as per the entered contest id. In order to get one, use <b>contstinf.py</b>.
  <li/>An email is sent to a recieving emailid, void of Subject, or any other specifications (which maybe modified in <i>message</i> variable of the function <i>send_email</i>).
  <li/>In order to treat the email as a reminder, the email is sent at the time of arrriving at the timestamp
  <li/>It is to be noted that the system must be kept on, and connected to the Internet until the timestamp is reached.
  <li/>Refer <a href="https://docs.python.org/2/library/smtplib.html">here</a> in case of timeout.
  <li/>In order to test the performance of the code, change the parameter of <i>time.sleep()</i> to a more suitable time(in seconds).
  <li/>I have not recruited the aid of online messaging, or email services since I didn't have an account for them, thereby disallowing me from testing my own code. Thus, I setup my own server.
