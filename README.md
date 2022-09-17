# DS200_module5
Data science visualisation page with scripts and plots


#------------------------DATA VISUALISATION USING MATPLOTLIB-------------------------#



==============Scatter Plot===================

Link for dataset: https://data.gov.in/resource/capacity-utilization-crude-steel-production-public-and-private-sector-india-2013-14-2018

Observations: 
A scatter plot is constructed to analyze the relationship between two features: production capacity vs. Actual production for a crude steel power plant. From the scatter plot, we observe that, in hindsight, there is a direct relationship between production capacity and actual production, i.e., production capacity increases with actual production. This is expected because, intuitively, we know that for an increased production demand of a commodity, production capacity has to increase to meet the required production demands. However, the relationship is not strictly linear, which is evident from an average value of R^2 = 0.602 obtained in this case.


Implementation: ScatterPlot_SteelProduction.py
Plot_file: Scatter_plot_example.pdf  

==============================================





==============Box Plot=======================

Dataset: https://data.gov.in/resource/all-india-consumer-price-index-ruralurban-upto-november-2021

Observations: 
A box plot is constructed for analyzing the variation of the consumer price index (CPI) for different agricultural commodities such as cereals, meat and fish, eggs, milk and milk products, oils and fats, fruits, vegetables, and pulses. Outliers are the maximum in the case of oils and fats. We have the maximum  CPI in the case of meat and fish. Oils and fats have the tightest grouping of data and are positively skewed, whereas pulses and products data is the least tight and is negatively skewed. Fruits CPI tends to a symmetrically distributed data.




Implementation: BoxPlot_agriproduce.py
Plot_file: Box_plot_example.pdf

============================================= 





================Line Plot====================== 

Link for dataset: https://data.gov.in/resource/category-wise-automobile-production-all-india-2012-13

Observations: 
A line plot is constructed for analyzing the production of different categories of automobiles in the entire country for the period 2001-2013. We consider five different categories of automobiles namely - Passenger vehicles (PVs), Heavy commercial vehicles (HCVs), Light commercial vehicles (LCVs), Three-wheelers (3Wh), and Two-wheelers (2Wh). In a hindsight, we observe rapid growth in the production of two-wheelers during this period. A possible reason for this is the rapid development of two-wheeler motorcycle technology which ensured a convenient, reliable, and low-cost commute option. Secondly, we observe a slower increase in the production of three-wheelers, heavy commercial vehicles, and light commercial vehicles. This is expected as this category of vehicles is primarily used for public transportation, goods, cargo transport, etc., and thus has a marginal increase in production demand. Finally, the production of passenger vehicles also shows a steady increase in production which is consistent with the fact that this category of vehicles is primarily used for personal uses and taxi services.




Implementation: LinePlot_AutomobileProduction.py 
Plot_file: Line_plot_example.pdf

=================================================


