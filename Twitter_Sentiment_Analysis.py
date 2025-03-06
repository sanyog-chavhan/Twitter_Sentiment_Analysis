# Databricks notebook source
# MAGIC %md
# MAGIC ### READING THE DATASETS

# COMMAND ----------

trump_df=  spark.read.format("csv").option("header", "true").option('inferSchema','true').option("quote", "\"").option("escape", "\"").option("multiline", True).load('/mnt/2024-team19/hashtag_donaldtrump.csv')

# COMMAND ----------

biden_df = spark.read.format("csv").option("header", "true").option("inferSchema","true").option("quote", "\"").option("escape", "\"").option("multiline", True).load("/mnt/2024-team19/hashtag_joebiden.csv")

# COMMAND ----------

# MAGIC %md
# MAGIC ### DATA EXPLORATION

# COMMAND ----------


print("Shape: ", trump_df.count(), " rows and ", len(trump_df.columns), " columns")
display(trump_df.head(10))


# COMMAND ----------

print("Shape: ", biden_df.count(), " rows and ", len(biden_df.columns), " columns")
display(biden_df)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Adding Column Hashtag

# COMMAND ----------

from pyspark.sql.functions import lit

# Creating a new column named 'hashtag' with the value 'Trump'
trump_df = trump_df.withColumn("hashtag", lit("Trump"))
 
display(trump_df)

# COMMAND ----------


from pyspark.sql.functions import lit
# Creating a new column named 'hashtag' with the value 'Trump'
biden_df = biden_df.withColumn("hashtag", lit("Biden"))
 
display(biden_df)

# COMMAND ----------

# MAGIC %md
# MAGIC ### MERGING BOTH THE DATAFRAMES

# COMMAND ----------

combined_df = trump_df.union(biden_df)

display(combined_df)

# COMMAND ----------

from pyspark.sql.functions import when
combined_df = combined_df.withColumn("country", when(combined_df["country"] == "United States of America", "United States").otherwise(combined_df["country"]))

# COMMAND ----------

# Showing the resulting DataFrames
display(combined_df)

# COMMAND ----------

# MAGIC %md
# MAGIC ### EXPLORATORY DATA ANALYSIS

# COMMAND ----------

# MAGIC %md
# MAGIC #### 1. COUNTRY MAP WITH MOST TWEET COUNT AND LIKES

# COMMAND ----------

from pyspark.sql.functions import col

# Dropping rows where 'country' is NULL in the filtered DataFrame
non_null_df = biden_df.dropna(subset=['country'])

# Grouping by 'country', count 'tweet', and ordering by the count
countries_map = non_null_df.groupBy('country') \
    .agg({'tweet': 'count'}) \
    .withColumnRenamed('count(tweet)', 'tweet_count') \
    .withColumnRenamed('sum(likes)', 'total_likes') \
    .orderBy(col('tweet_count').desc()) \
    

display(countries_map)

# COMMAND ----------

# MAGIC %md
# MAGIC ####2. TOP 5 COUNTRIES WITH TWEET COUNTS FOR BIDEN

# COMMAND ----------

from pyspark.sql.functions import col, sum

# Filtering where 'hashtag' is 'biden'
biden_df = combined_df.filter(col('hashtag') == 'Biden')

# Dropping rows where 'country' is NULL in the filtered DataFrame
non_null_df = biden_df.dropna(subset=['country'])

# Grouping by 'country', count 'tweet', sum 'likes', and ordering by the count
top_countries_biden = non_null_df.groupBy('country') \
    .agg({'tweet': 'count'}) \
    .withColumnRenamed('count(tweet)', 'tweet_count') \
    .orderBy(col('tweet_count').desc()) \
    .limit(5)

# Displaying the top 10 countries where 'hashtag' is 'biden'
display(top_countries_biden)

# COMMAND ----------

# MAGIC %md
# MAGIC #### 3. TOP 5 COUNTRIES WITH TWEET COUNTS FOR TRUMP

# COMMAND ----------


# Filtering where 'hashtag' is 'Trump'
trump_df = combined_df.filter(col('hashtag') == 'Trump')

# Dropping rows where 'country' is NULL in the filtered DataFrame
non_null_df = trump_df.dropna(subset=['country'])

# Grouping by 'country', count 'tweet', sum 'likes', and ordering by the count
top_countries_trump = non_null_df.groupBy('country') \
    .agg({'tweet': 'count'}) \
    .withColumnRenamed('count(tweet)', 'tweet_count') \
    .orderBy(col('tweet_count').desc()) \
    .limit(5)

# Displaying the top 10 countries where 'hashtag' is 'trump'
display(top_countries_trump)

# COMMAND ----------

# MAGIC %md
# MAGIC #### 4. Top 5 states for Tweet Counts for Biden

# COMMAND ----------

from pyspark.sql.functions import col, sum

# Filtering where 'hashtag' is 'biden'
biden_df = combined_df.filter(col('hashtag') == 'Biden')

# Dropping rows where 'country' is NULL in the filtered DataFrame
non_null_df = biden_df.dropna(subset=['state'])

# Grouping by 'country', count 'tweet', sum 'likes', and ordering by the count
top_state_biden = non_null_df.groupBy('state') \
    .agg({'tweet': 'count'}) \
    .withColumnRenamed('count(tweet)', 'tweet_count') \
    .orderBy(col('tweet_count').desc()) \
    .limit(5)

# Displaying the top 5 states where 'hashtag' is 'biden'
display(top_state_biden)

# COMMAND ----------

# MAGIC %md
# MAGIC #### 5. Top 5 states for Tweet Counts for Trump

# COMMAND ----------

from pyspark.sql.functions import col, sum

# Filtering where 'hashtag' is 'biden'
trump_df = combined_df.filter(col('hashtag') == 'Trump')

# Dropping rows where 'country' is NULL in the filtered DataFrame
non_null_df = trump_df.dropna(subset=['state'])

# Grouping by 'country', count 'tweet', sum 'likes', and ordering by the count
top_state_trump = non_null_df.groupBy('state') \
    .agg({'tweet': 'count'}) \
    .withColumnRenamed('count(tweet)', 'tweet_count') \
    .orderBy(col('tweet_count').desc()) \
    .limit(5)

# Displaying the top 5 states where 'hashtag' is 'trump'
display(top_state_trump)

# COMMAND ----------

# MAGIC %md
# MAGIC #### 6. TOP 5 COUNTRIES WITH MOST LIKES FOR BIDEN

# COMMAND ----------

# Filtering where 'hashtag' is 'biden'
biden_df = combined_df.filter(col('hashtag') == 'Biden')

# Dropping rows where 'country' is NULL in the filtered DataFrame
non_null_df = biden_df.dropna(subset=['country'])

# Grouping by 'country', count 'tweet', and order by the count
top_countries_biden = non_null_df.groupBy('country') \
    .agg({'likes': 'sum'}) \
    .withColumnRenamed('sum(likes)', 'likes_count') \
    .orderBy(col('likes_count').desc()) \
    .limit(5)

# Displaying the top 5 countries  and where 'hashtag' is 'biden'
display(top_countries_biden)

# COMMAND ----------

# MAGIC %md
# MAGIC #### 7. TOP 5 COUNTRIES WITH MOST LIKES FOR TRUMP

# COMMAND ----------

# Filtering where 'hashtag' is 'biden'
trump_df = combined_df.filter(col('hashtag') == 'Trump')

# Dropping rows where 'country' is NULL in the filtered DataFrame
non_null_df = trump_df.dropna(subset=['country'])

# Grouping by 'country', count 'tweet', and order by the count
top_countries = non_null_df.groupBy('country') \
    .agg({'likes': 'sum'}) \
    .withColumnRenamed('sum(likes)', 'likes_count') \
    .orderBy(col('likes_count').desc()) \
    .limit(5)

# Displaying the top 5 countries  and where 'hashtag' is 'Trump'
display(top_countries)

# COMMAND ----------

# MAGIC %md
# MAGIC #### 8. TOP 5 SOURCES WITH MOST TWEET COUNTS FOR BIDEN

# COMMAND ----------


# Filtering where 'hashtag' is 'biden'
biden_df = combined_df.filter(col('hashtag') == 'Biden')

# Dropping rows where 'country' is NULL
non_null_df = biden_df.dropna(subset=['source'])

# Group by 'country', count 'tweet', and order by the count
top_source = non_null_df.groupBy('source') \
    .agg({'tweet': 'count'}) \
    .withColumnRenamed('count(tweet)', 'tweet_count') \
    .orderBy(col('tweet_count').desc()) \
    .limit(5)

# Display the top 5 sources for Biden
display(top_source)

# COMMAND ----------

# MAGIC %md
# MAGIC #### 9. TOP 5 SOURCES WITH MOST TWEET COUNTS FOR TRUMP

# COMMAND ----------


# Filtering where 'hashtag' is 'trump'
trump_df = combined_df.filter(col('hashtag') == 'Trump')

# Dropping rows where 'country' is NULL
non_null_df = trump_df.dropna(subset=['source'])

# Group by 'country', count 'tweet', and order by the count
top_source = non_null_df.groupBy('source') \
    .agg({'tweet': 'count'}) \
    .withColumnRenamed('count(tweet)', 'tweet_count') \
    .orderBy(col('tweet_count').desc()) \
    .limit(5)

# Display the top 5 sources for Biden
display(top_source)

# COMMAND ----------

# MAGIC %md
# MAGIC ### BIDEN

# COMMAND ----------

display("BIDEN")

# COMMAND ----------

# MAGIC %md
# MAGIC ### TRUMP

# COMMAND ----------

display("TRUMP")

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC
