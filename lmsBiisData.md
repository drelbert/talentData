//LMS data  manual extract from UI
to get all employees training records
HHS Train>HHS Training Completions by Offering Domain Report>date
(from 10/1/17 on check "Include Sub Domains")
and also
check HHS Common Domain for all Skill Soft and Mandatory
Select R (for HRSA top level org code)

to get all course offerings
catalog>offerings>date range>
can query by delivery type to get completion status (ie delivered, canceled, etc)

//Conversations
Convo Nathan Knight
from 2013 on, data was not replicable on biis system
this means, not all data elements are present

huge amount of data so
GP asked opdivs what they wanted
users said they wanted X which was on screen
then gp sent over only this data to BIIS

daily (6days/week) 72 updates to tables or full tables

issue = biis does not have the data so they can confidently send that data out to the opdiv requestor

gp issue, they have far too complex data (according to them)

the current ask is = send us the data as is, 'send it all'
and
assit biis in replicating reports

current state GP and biis are ironing out what biis will actually get

SQLServer(GP) to oracle(BIIS)

ETL options
self service = access so I can build reports
or
biis could build reports and then I download (precanned, crystal)
or
request biis interface to get data weekly or whatever


what can we do to help?  

Who to talk with next?
George Chambers Acting Dir of OEAD
Jack Stout Sol Del OEAD

Next
Darlene Young
BIIS Director for OEAD
what was outcome of meeting w/GP Dec 8?

Joan Bernal
Laison with GP
James Gonzales
Laison with GP


Convo w GP 1/3
Ed = Program Manager
Kathy White = Bus Analyst
Janet =
Mike = engineer


How might we access lms data in a raw format at regular intervals?

Data pull or dump that is in raw format
vs something that is formatted or normalized to be used in crystal reports

request from HHS/BIIS for all LMS Data
so direct access to ALL denormalized data  

point = someone in HR at HHS(?) level has requested LMS data  

GP Proposed to BIIS
nightly export of all raw data
or
set up server and access via vpn pipe to build crystal reports

options for tranfer of data now:
one = get data dump of all learner records for FY 17 and 18 from BIIS
two = obtain data directly from GP with approval from James/Alvin

other option
three = maybe access to drop box?  this may need an IAA

Convo w Nathan K, Ragu, Gobi, Lloyd
biis was getting denomalized tables
instead of 500 tables, got 100
when doing dev of a report, some data was missing  

to be delivered
one  75 tables of lms data
two four crystal reports with lms data  
