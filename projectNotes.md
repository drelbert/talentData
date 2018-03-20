//insight through access

the stack
flask web micro framework
Flask-SQLAlchemy
jinja2 handles the view
mysql

server-model-view-templates


when creating the template, first write the {{row.whatever}} to establish the view

then work on the href for the calling of the data =
one  the right path to the app.route in server.py ""/somehting/...

two  the sql based data for the ...{{row.something}}" part of the link


how does jinja work?

//count work and injecting data to index.html

<table>
<thead>
    <tr>
      <th scope="col">H1, H2, meta, etc.</th>
    </tr>
</thead>
<tbody>
  {% for rownum, row in queryNameHere.iterrows() %}
    <tr>
          <td>{{row.ColumnNameHere}}</td>
    </tr>
  {% endfor %}
  </tbody>
</table>



//starting server.py in command prompt
nav to folder
'>' cd \Desktop\coLab\project\app
use
python server.py

task kill
tasklist : findstr pyt
taskkill /F /PID '11184' or what ever PID is

one = practical app that solves use case
two = mine data for patterns
three = build model to show insights
four = generate visualization


//term command to end MAMP server
C:\Users\DElbert>taskkill /F /pid 7768



//visualization
plotly  


//db notes
//general table constraints
primary key = a column serve as unique identifier for each row of data (not null and duplicate)
foreign key = a column that corresponds to a primary key in another table to cross reference between tables
   fk relations = ensure and enforce rel between tables
   example:
   if fk on transcript table then cannot add record that is not cross-ref in the main person table

index = stores indexed values from one or more columns to get data quickly from a table

//Mandatory courses
EEO Awareness Training for HHS
Freedom of Information Act (FOIA) Training for Federal Employees
2017 Counterintelligence Insider Threat Awareness
HHS Cybersecurity Awareness Training
FY2017 Cybersecurity Awareness Training
HHS 2017 Records Management
Introduction to Counterintelligence and Insider Threat
Section I: Occupant Emergency
Section II: Continuity Awareness
Section III: Personal Preparedness

//Build Notes
2.12 to 2.23
obtained updated data
AY 17 and 18
employees completed
courses offered
continuing ed plan courses
supervisor list
supervisor courses
custom engagement data

//Notes on Meeting w Dan
what puzzles me


what other data validation info do I need?

how to load CY 18 but maintain division between that an CY17?

how to reduce the time for virtualClassParticipants query?
now the mysql duration is 4.8 seconds
response
add an index to the deliveryType  
