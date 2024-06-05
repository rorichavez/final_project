
![hello](https://cdn.prod.website-files.com/63f6e52346a353ca1752970e/6440bf1a87dd9331e54024e7_study-cover-bumble.jpeg)

# Bumble: Partner Acquisition Analysis
> _Generate revenue through client acquisition_
----

## 1. Libraries and Data used:
1.1 Libraries: <br>
    
    - seaborn 
    - matplotlib 
    - pandas
    - numpy
    - time
    - warnings
    - requests 
    - selenium
    - re
    - unicodedata
    - wordcloud 
    
1.2 Data source: 
> Bumble:<br> [Bumble Web](https://fr1.bumble.com/get-started)


**Profiles:**
- Women: 27 year old with tastes: everyone, who lives in Barcelona. Maximum and minimum age range.
- Men: 27 year old with tastes: everyone, who lives in Barcelona. Maximum and minimum age range.
    

## 2. Data Cleaning Documentation: 
![tags](https://res.cloudinary.com/apartmentlist/image/fetch/f_auto,q_auto,t_renter_life_article/https://images.ctfassets.net/jeox55pd4d8n/7LmVkTOXPiCFRLBFiCk96K/dfd4f69f0b3b54e88d2bbb168d6186f0/Press_Date_Interest_Badges_US__Sourced_2.4.22___1_.png)

2.1. Add “profile” column to indicate whether the profile is female or male <br>

2.2. Drop duplicate rows <br>

2.3. Merged both (women & men) datasets: <br>
    - Change columns names <br>
    - Remove "cm" in column height so is a int number <br>
    - Remove "Barcelona" in column location so I only take the town <br>
    - Looking for duplicate column (taking into account that the profile of the column “profile” makes them different so I have to filter not taking into account this column) <br>
    - Use regex to make the job column more available <br>

2.4. Visualization of more repitet words in about_me colums: <br>
    - Define stop words in English and Spanish <br>
    - Define specific words to be deleted <br>
    - Remove NaN values and 'NaN' strings <br>
    - Convert all values to text strings <br>
    - Remove spaces at the beginning and end of each string, convert to lowercase and replace <br>
    - Removing punctuation marks <br>
    - Function to remove stop words from a text <br>
    - Function to generate a word cloud <br>
    - Define specific words to be deleted <br>

2.5. Documentation:

    - name: the name under which the user registered, it does not have to be the real one, it can be a nickname 
    - age: the user's age
    - location: where the user is at the moment he/she registered
    - story_about: short description that the user wrote about him/herself 
    - job: the user's profession or where he/she works 
    - education: where the user has studied or type of education he/she has
    - height: the user's height 
    - intentions: what the user is looking for in the application at the relationship level 
    - exercise: how often the user exercises    
    - educationTag: what level of education the user has 
    - drinking: how often or if the user drinks    
    - smoking: how often the user smokes or if he/she does 
    - childrens: what family plans the user has 
    - religion: what religion the user practices  
    - politics: what political ideology the user has  
    - gender: the type of gender with which the user identifies       
    - zodiacSign: the user's zodiac sign
    - profile: indicates whether the user was extracted from the “woman” or “man” profile

## 3. Data Exploration & Visualization
![match](https://techcrunch.com/wp-content/uploads/2022/11/Compliments-Press-Image.png?w=1024)

3.1. Generate general gender view by profiles <br>
3.2. Display by gender “women” and “men”: age group, location, jobs and education <br>
3.3. Display by gender “women” and “men” separately the percentage by subcategory in categories such as: Family Plans and Lifestyle <br>
3.4. Visualization by gender “women” and “men”: idiologies (taking into account: religion, politics and zodiac sign) <br>
3.5. Display the most repeated words according to the about me of the profiles <br>
> FIND THE VISUALIZATIONS:<br> [Tableau](https://public.tableau.com/app/profile/roraima.chavez/viz/bumble/bumble?publish=yes)



## 4. Analysis & Conclusion
![bumble](https://bumble-buzz.com/wp-content/uploads/2024/04/relaunch-bumble.png?w=628&h=460&crop=1.jpeg)
> VISUALIZATIONS:<br> [Tableau](https://public.tableau.com/app/profile/roraima.chavez/viz/bumble/bumble?publish=yes)

## <span style="color:darkslateblue"> Identifying Potential Partners Aligned with User Interests </span>

Choose partners that are related to the users' interests. For example:

- **Food:** Partner with restaurants, food delivery services, cooking class providers.

- **Music:** Partner with music streaming platforms, concert venues, merchandising retailers, instrument stores or festivals. 

- **Travel:** Partner with airlines, hotels, travel agencies, tour operators or local attractions based on users' travel destinations, preferred activities (e.g. adventure travel, cultural experiences).

- **Sports:** Partner with sports teams, sportswear brands, sporting goods retailers or gyms. Even host sporting events. 

- **Film and art:** Partner with movie studios, art galleries, museums, streaming services with a strong movie collection or ticketing platforms.


## <span style="color:darkslateblue"> Partner Selection Based on User Demographics and Ideologies </span>

When selecting partners, it is crucial to consider specific demographics and ideologies. This involves understanding the age distribution, gender balance, geographic distribution, predominant interests and general ideological leanings of your users. 

By prioritizing partners who fit these characteristics, you can ensure that partnerships resonate with your audience and increase the overall appeal of your events.


### <span style="color:darkslategrey"> Non-Invasive Promotion for Female Users </span>

Given the smaller female user base, it is essential to take a non-intrusive approach to promoting new partners, especially to female users. 

Avoid overwhelming or discouraging female users with excessive promotion, as this may hinder their willingness to participate in the application. Instead, focus on creating a welcoming and inclusive environment that attracts and retains users.


## <span style="color:darkslateblue"> Mutually Beneficial Partnerships </span>

Look for partners with whom you can collaborate on events or promotions that bring mutual benefits to both parties. 

This win-win approach ensures that your partnerships not only enhance the user experience, but also bring value to your partners. Think about co-branded events, exclusive offers or joint marketing campaigns that benefit both your users and your partners.


![thanku](https://team.bumble.com/social-sharing.jpg)
### Thank you!

