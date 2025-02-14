CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;


-- All dogs with parents ordered by decreasing height of their parent
create table by_parent_height_helper as 
  select name, parent, height 
from dogs, parents where name = child;

CREATE TABLE by_parent_height_helper02 AS
  select a.name as name, a.parent as parent, b.height as parent_height
from by_parent_height_helper as a, dogs as b where a.parent = b.name
;

CREATE TABLE by_parent_height AS
select name 
from by_parent_height_helper02 order by parent_height desc
;


-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name, size
from dogs, sizes where height > min and height <= max 
;


-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT a.child as first_child, b.child as second_child
from parents as a, parents as b where a.parent = b.parent and a.child < b.child
;

-- Sentences about siblings that are the same size
create table sentences_helper as 
  select first_child, second_child, size as first_child_size
from siblings, size_of_dogs where first_child = name
;
create table sentences_helper02 as
  select first_child, second_child, first_child_size, size as second_child_size
  from sentences_helper, size_of_dogs where second_child = name;
CREATE TABLE sentences AS
  SELECT "The two siblings, " || first_child || " and " || second_child || ", have the same size: " || first_child_size
from sentences_helper02 where first_child_size = second_child_size
;


-- Height range for each fur type where all of the heights differ by no more than 30% from the average height
create table range as
  select fur, min(height) as min, max(height) as max, avg(height) as avg, avg(height) - 0.3 * avg(height) as avg_min, avg(height) + 0.3 * avg(height) as avg_max
from dogs group by fur;
create table low_variance_helper as 
  select fur, min(height) as min, max(height) as max
from dogs group by fur 
;

CREATE TABLE low_variance AS
  select a.fur, a.max - a.min
from range as a, low_variance_helper as b where a.fur = b.fur and b.min >= avg_min and b.max <= avg_max
;
