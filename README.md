# Empirical-Investigation_P4_public
COP3502_C Final Project(4) : Investigate a Scientific Hypothesis and visualize your findings


Empirical Investigation Group 54: Project Showcase

What dataset did you use? 
We utilized the “Death rates for suicide, by sex, race, Hispanic origin, and age: United States, selected years 1950–2018” dataset from the Centers for Disease Control and Prevention (CDC). The National Center for Health Statistics provided this dataset to the CDC and was last updated in April of 2022. These rates were derived from deaths per 100,000 residents in the United States.

What was your hypothesis/question? 
Each member of our team curated a hypothesis based on the data set we chose to analyze. Megan hypothesized that the most common race and gender to commit suicide in the United States is white males. Jellane hypothesized that the lowest amount of suicides occurred in the population of Asian and Pacific Islanders. Emiliano’s hypothesis was that the difference in suicide death rates between the compared age ranges would show that the younger males would have higher death rates in recent years. Nora’s hypothesis was that white older males in the United States would have a higher overall trend of suicide rates in the most recent years,
From these options, our team focused on analyzing a variation of Megan and Emiliano's hypothesis which covered the comparison between the rates of death by suicide from Males of all races aged 25 to 44 and Males of all races aged 45 to 64.



How did you approach the analysis? [describe the statistical measures and libraries you used] 
We approached the analysis using the Pandas Python library to analyze, clean, and manipulate the established dataset. For the analysis we configured the code to drop rows where a column had “NaN” or empty values to allow for a more standardized model. Additionally, only relevant columns in the dataset were selected to be sorted which included: ‘STUB_NAME', 'STUB_LABEL', 'AGE', 'YEAR', and 'ESTIMATE'. Once the selected columns of data were correctly sorted, a predetermined subset of the organized data would be displayed in the terminal.

How did you visualize your results? [describe the visualization libraries and add screenshots of visualization]
We visualized the results of our data organization by inputting empirical data from the imported data set into a visual bar chart using Matplotlib. We made individual functions to represent each data model/ graph we desired to make. We used Matplotlib functions to use the data we loaded and organize it into a visual chart.
