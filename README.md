🏙️ *Half a Medium* — A Rails App That Reflects People Through Cities🧠
Core Idea

This app is *not powered by AI*, but by *intentional database design*. Each
*city* in the app is a *semantic container*—a place where people appear not
randomly, but through *queries that reflect your vision* of how humans
move, gather, and express themselves.

You’re not predicting behavior. You’re *curating presence*.
🛠️ Technical ArchitectureModels

   -

   User: traveler, storyteller
   -

   Journey: a collection of entries tied to a user
   -

   Entry: timestamped moment with photo, location, and reflection
   -

   City: geographic anchor with attached logic
   -

   Appearance: a join model that links users to cities via queries

Database Views

Each city has a *custom SQL view* that defines:

   -

   Who appears in that city (based on timestamp, location proximity, or
   thematic tags)
   -

   How they appear (e.g., sorted by time of day, grouped by emotion,
   filtered by language)
   -

   What stories are visible (e.g., only journeys that include a photo and a
   reflection)

sql

CREATE VIEW city_appearances AS
SELECT users.id, journeys.id, entries.timestamp, entries.photo_url
FROM entries
JOIN journeys ON entries.journey_id = journeys.id
JOIN users ON journeys.user_id = users.id
WHERE entries.city_id = cities.id
AND entries.timestamp BETWEEN cities.start_time AND cities.end_time;

This view becomes the *medium*—not artificial intelligence, but *human
intelligence encoded in SQL*.
🖼️ Rails Templates as Mirrors

Your Rails views (.erb or .haml) don’t just render data—they *manifest
people*. Each template is a *reflection of your query logic*, showing users
as you’ve chosen to reveal them
- back end developer that befriends with the front end developer
- 
