# fake_data

How Easy it is to Create Fake Covid-19 Data
Max Bade
Max Bade
Aug 3 · 5 min read





Image for post
A Fake Graph with Fake Data Alleging HCQ is 2x More Likely to Cause Death in Patients with Covid-19
I usually wouldn’t produce a story like this, but it has to be said, and if it isn’t me, a free thinking data engineer/data scientist, with minimal bias towards either side and an eye for seeing through the bs, producing it, I don’t know who will.
Covid-19 Fake HCQ Trial Data Background
Recently an article came out highlighting the inconsistencies and down right impossibilities of a hydroxycholoroquine study that “proved” the drug was 2x more likely to increase the risk of cardio vascular issues in patients with covid-19.
Image for post
Surgisphere’s wikipedia page as of today 8/3/2020
The “trial” by a now defunct company called Surgisphere with no website, no CEO, no employees, previous employees on linkedin who’s profiles have suddenly vanished, and of said previous employees were a sci-fi writer and a likely model-for-hire, allegedly had over 150k human results in their hyrdroxycholoroquine trial. When asked to reproduce 15k results/rows from the trial results/data, they could not.
Image for post
So What Does This Mean?
In simple terms, it means the american public was lied to by Dr. Fauci and two world-leading medical journals: the Lancet and the New England Journal of Medicine, into believing and promoting a recommendation to lawmakers and the general public that an extremely cheap and effective drug in which the world has been using since the 1940s, was unsafe and ineffective in treating covid-19. This has undoubtedly lead to tens of thousands of unnecessary deaths as doctors were not able to prescribe the potentially life-saving drug for early-stage covid-19 patients.
So How Easy is it to Falsify Data?
*For the sake of simplicity, dataframe will be used in place of database They’re fairly similar. A dataframe is an in-memory data structure in which we store data. Dataframes can be exported and imported into a database in many ways — automatically via script, imported via csv, scheduled via ETL etc. Thus, database is the ultimate home of our data, dataframes are what we work with to manipulate the data and do analysis.
To mimic what the likely shell company Surgisphere did to create this “trial”, I’m going to show you just how easy it is to create fake data and push out an baseless narrative.
Import libraries and Formatting
Importing pandas, numpy and plotly namely for data manipulation and visualization, as well as adjusting the formatting/output of the jupyter notebook cells.
Image for post
Data libraries
Create Fake Columns with Fake Data
Creating a patient, days_since_covid started and an is_dead column to further validate this dataframe.
Image for post
We create lists with fake numbers to later add to the dataframe
Create a Fake Dataframe with Random Number Generated Columns
This is it. All we needed was bout 20 lines of code and we have an entirely fake dataframe with scary sounding columns like is_dead and days_since_covid.
Image for post
That’s it.
Image for post
Output
To Take it a Few Steps Further
Below is a dataframe with decimals in columns rather than whole numbers. Just to make it more believable.
Image for post
Decimals in dataframe
Presentation Mode
What if we had to present the data — we might want to make it look pretty. Here’s our fake data looking pretty:
Image for post
style.background_gradient(cmap=’Blues’)
Make our Data Look Like it’s Increasing
Now say we wanted to make our data appear as if it’s increasing. Well that’s easy, I didn’t create a function to do this programmatically, but we can just make a few dataframes and join them together at the end. Each dataframe will consist of slightly higher numbers (around 5% higher on average).
Image for post
Add in our Scary Columns and show info()
Add in the columns we made for the earlier dataframes.
Image for post
Dataframe info() at the top and gradually increasing dataframe at the bottom
Drive it Home — Plotting our Fake Data
Bam, we have a gradually increasing covid-19 hcq trial-like dataframe; in under 100 lines of code. The only thing left to do at this point would be to insert our data into a database and share the database credentials with whoever needs access.
Image for post
We could have made the line less smooth, but this is just an example that took less than an hour to create
What Does All of this Mean?
If you’re a data junkie like me, you’re weary of pretty much any statistic. Especially the ones produced by the government. Your takeaway from this should be — any data can be falsified incredibly easily. You are not safe from misinformation or false narratives from falsified data ever. But there is hope. You have to use the big beautiful brain god or whoever your higher power is, gave you, to question, think critically and ultimately seek out people you trust. We don’t often have time to research and fact-check everything we hear in the news, but thankfully, there are people who make a living doing just that. Below are a few of my favorite pages for information:
Best Resources for Accurate News Information
Breitbart
No Mercy Podcast
Coast to Coast am Radio
Tim Pool Podcast
Joe Rogan Podcast
Qanon pages (twitter and instagram)
https://www.instagram.com/wwg1wga_/?hl=en
https://www.instagram.com/qthewakeup/?hl=en
https://www.instagram.com/q_pill/?hl=en
https://www.instagram.com/sheepn0more/?hl=en
If you’d like to support my work, feel free to buy me a coffee, or follow me on social media.
Image for post
Thanks,
Max
