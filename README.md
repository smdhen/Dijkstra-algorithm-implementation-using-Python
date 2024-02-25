# <center>Formula 1 World Championship DataWarehouse-1950--2022.</center>

![Screenshot from 2024-02-22 18-08-49](https://github.com/smdhen/Formula-1-World-Championship-Data-Warehouse-1950---2022-/assets/96498289/68a6193e-b353-4c31-8bed-4b5217e59acd)

## Table of contents
- [Project Overview](#project-overview)
- [Data description](#data-description)
- [Tools](#tools)
- [Datawarehouse design](#datawarehouse-design)
- [Feeding the dimensions tables](#feeding-the-dimensions-tables)
- [Feeding the Fact tables](#feeding-the-fact-tables)
- [Results](#results)
- [Dashboard analysis ideas](#dashboard-analysis-ideas)
- [Summary](#summary)

### Project Overview

This project involves the creation of a Data Warehouse using [Talend Open Studio](https://www.talend.com/products/talend-open-studio/)  and the visualization of data through graphs using [Tableau](https://www.tableau.com/). 

### Data description 

- Context

Formula 1 (F1 or Formula One) is the highest class of single-seater auto racing sanctioned by the Fédération Internationale de l'Automobile (FIA) and owned by the Formula One Group. The FIA Formula One World Championship has been one of the premier forms of racing around the world since its inaugural season in 1950. 

- Content

The dataset consists of all information on the Formula 1 races, drivers, constructors, qualifying, circuits, lap times, pit stops, championships from 1950 till the latest 2023 season.

Here is the [Link](https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020) to dataset.

### Tools 

1. Excel : Data Cleaning 
2. Talend : Decision-Making Data Processing
3. Tableu Creating Reorts
4. sqlServer :  Data base --> (star schema)

### Datawarehouse design:

The datawarehouse will contain 5 dimensions: dimDate, dimDriver, dimConstructor, dimCircuit, dimRace, and a fact table: factResults.
We will focus on the following KPIs (Key Performance Indicators) : Points, Laps, FastestLapSpeed, FastestLapTime, Rank.

The star schema is illustrated in the following figure.

![Screenshot from 2024-02-22 18-20-26](https://github.com/smdhen/Formula-1-World-Championship-Data-Warehouse-1950---2022-/assets/96498289/917ba6ee-5227-4d1f-ab32-76dedb8a4343)

### Feeding the dimensions tables:

- dimDriver

 ![Screenshot from 2024-02-22 18-28-19](https://github.com/smdhen/Formula-1-World-Championship-Data-Warehouse-1950---2022-/assets/96498289/f8bfda42-80ba-4d70-b699-92cb68329c7a)
  
- DimConstructor

 ![Screenshot from 2024-02-22 18-29-08](https://github.com/smdhen/Formula-1-World-Championship-Data-Warehouse-1950---2022-/assets/96498289/13ce1f58-c654-41f3-8b4e-23dc1f6ef555)

- dimCircuit

![Screenshot from 2024-02-22 18-29-52](https://github.com/smdhen/Formula-1-World-Championship-Data-Warehouse-1950---2022-/assets/96498289/8eb2c3e0-a12a-4883-b8cb-85e590cadb63)

- dimRace
  job -4
- dimDate:
  job -5
### Feeding the Fact tables:
![Screenshot from 2024-02-22 18-31-20](https://github.com/smdhen/Formula-1-World-Championship-Data-Warehouse-1950---2022-/assets/96498289/4b68608c-d423-4ae2-aeb3-d79e05f8fdae)

### Results
20 first lines : 

![Screenshot from 2024-02-22 18-38-29](https://github.com/smdhen/Formula-1-World-Championship-Data-Warehouse-1950---2022-/assets/96498289/0a72cd2d-8475-4235-b42b-850038d0b534)


Having the same raceId, idDate, and circuitId is not problematic because all drivers participate in the same race happening on the same date, at the same circuit, but they will have different results (KPIs).

### Dashboard analysis ideas
Here are some visualization graphs created using Tableau.

1. The Formula 1 car manufacturers based on the cumulative sum of points earned by their cars. This provides an overview of the performance of each manufacturer in terms of points.
2. The second graph can displays the cumulative points of each driver over time, allowing for an understanding of the drivers' performance trends. By analyzing this graph, a manufacturer can select drivers whose points consistently improve over the years.
![Screenshot from 2024-02-22 18-59-55](https://github.com/smdhen/Formula-1-World-Championship-Data-Warehouse-1950---2022-/assets/96498289/6bc0e049-0f13-46db-bc5f-131d2976eca1)

3. The next graph illustrates the rankings of drivers from different manufacturer teams over time. This helps identify the performance of drivers within their respective teams
![Screenshot from 2024-02-22 19-05-01](https://github.com/smdhen/Formula-1-World-Championship-Data-Warehouse-1950---2022-/assets/96498289/c8e3151e-33bc-455f-b0b3-ed06dcf30c00)

4. Lastly, the graph shows the number of laps completed by drivers, categorized by circuit, along with their fastest lap speeds over time. This information allows manufacturers to identify the circuits that best suit each driver based on their number of laps and speed.
![Screenshot from 2024-02-22 19-04-31](https://github.com/smdhen/Formula-1-World-Championship-Data-Warehouse-1950---2022-/assets/96498289/cb94c68e-f41d-48d2-84e7-e67a99ba735d)

### Summary
This project combines data analysis and visualization techniques to gain insights into the performance of car manufacturers, drivers, and their compatibility with specific circuits.
