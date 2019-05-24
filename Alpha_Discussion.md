Alpha will be done until 5/26/2019

Problem: There are times when people want to watch a movie suddenly. To do that, first they have to open the map and search for a cinema nearby. After that they have to check the movie schedule of each cinema nearby and this is a very troublesome work and takes time. Thus, our team decided to make a solution.

Objective: Let the user select the movie they want to watch and suggest the fastest way to watch the movie. This will be done by calculating the distance between the user and the cinema but also by checking the screening time of several cinemas nearby the user using location-based service from map api and cinema screening time api.

Alpha will contain
major function running but not everything

Only 30 cinemas from CGV in Seoul will be available
DB will be updated each day (24hours)
- made by python
Server will be done by AWS
However DB of cinema seats will be updated by user request

Map API - Naver Map API
problem right now is can't express the pedestrian route

UI design will have specific size - the Alpha's Alpha will be done by basic elements in Android Studio
until this week(5/19) our goal will be finishing the Alpha's Alpha
+DB test putting the data crawled to the server and test if it works
Specific UI will be done for final DEMO

The list of cinemas nearby will show cinemas in certain radius however if there is a cinema that has earlier screening time
we will use the algorithm that we proposed and recommend the fastest way to watch the certain movie

Some parts may not be implemented (will be added while developing)
For Alpha version the algorithm of finding the fastest cinema will be excluded
The best cinema will be selected only by the closest cinema reachable by public transport 

Bug Issues will be updated in our LookVie github/Issues
Email bug report to hansnam123@gmail.com. We will appreciate explanation with screenshots
