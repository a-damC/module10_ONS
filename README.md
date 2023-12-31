# module10_ONS
Visual data on cost of living

The U.K. has had an issue with inflation for the last couple of years.
-
[Looking at the inflation graph](https://github.com/a-damC/module10_ONS/blob/main/pdfs_main/inflation_last_5_years.pdf) we can see the Bank of England's 2% aim was surpassed as the U.K. exited 
Lockdown measures as demand increased and supply side issues could not keep up. The Russian invasion 
of Ukraine compounded inflation problems as energy and grain resources became reduced due to embargoes 
placed on Russia and the decimation of the Ukrainian grain trade routes.
Further economic instability was introduced by Liz Truss's Mini-budget.



The Input-Output Table
-
[The increase in energy prices](https://www.ons.gov.uk/economy/inflationandpriceindices/articles/theenergyintensityoftheconsumerpricesindex/2022) have many businesses and households worried
about the future.
[The Input-Output Table](https://github.com/a-damC/module10_ONS/blob/main/data/clean_IOT_data.csv) shows the value in million of pounds of how each industry's outputs are dependent on other
industry's output for input.

[Here is a Heatmap](https://github.com/a-damC/module10_ONS/blob/main/pdfs_main/figure2_IOT_heatmap.pdf) visualisting this data.
It can be seen here some industries are very dependent on a lot of others industries such as construction,public administration, and less so education.


July 2023 price lists
-
[Looking at the price listings of the CPI basket of goods](https://www.ons.gov.uk/economy/inflationandpriceindices/datasets/consumerpriceindicescpiandretailpricesindexrpiitemindicesandpricequotes) we can look at the different regions of the U.K. and see how the price of basic goods differs.
There are boxplots for all the goods located [here](https://github.com/a-damC/module10_ONS/tree/main/boxplot_per_item)

The different numbers relate to the following regions [(and can be found here)](https://github.com/a-damC/module10_ONS/blob/main/data/glossaryrevised.xls):

1 = Catalogue collections\
2 = London\
3 = SE\
4 = SW\
5 = East Anglia\
6 = East Midlands\
7  = West Midlands\
8 = Yorks & Humber\
9 = NW\
10 = North\
11 = Wales\
12 = Scotland\
13 = NI\


Some interest boxplots are as follows:\
[Bread price ranges across the U.K.](https://github.com/a-damC/module10_ONS/blob/main/pdfs_main/breads_july2023_compare.pdf)\
[BLT price ranges across the U.K.](https://github.com/a-damC/module10_ONS/blob/main/pdfs_main/BLT_july2023_compare.pdf)\
[Take-away price ranges across the U.K.](https://github.com/a-damC/module10_ONS/blob/main/pdfs_main/takeaway_july2023_compare.pdf)\



Techniques Practiced and Issues
-
During this training I created a heatmap for the first time. This took a long time as I initially tried in R but relented and wrote it in python 
as I found it hard to loop over the variables I wanted in R.
\
I did improve my R skills but I had to relearn a lot as I had not used it for a while and this did hinder any attempts at doing more complex tasks such as ML which I wished to have engaged in.
\
I also had to re-setup my Github account and that took some time to figure out how this all worked!!!
\
Looking forward to Year2
\
Thank you for reading - Adam Crewdson


