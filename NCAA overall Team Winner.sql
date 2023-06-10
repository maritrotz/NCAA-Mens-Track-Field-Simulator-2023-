use ncaatrack;

SELECT Team, SUM(Points) AS TotalPoints
FROM (
  SELECT Team,points FROM  ncaatrack.top_8_10000m -- 1 -- 
  UNION ALL
  SELECT Team, points FROM top_8_100m  -- 2 --
  UNION ALL
  SELECT Team, points FROM top_8_110h  -- 3 --
  UNION ALL
  SELECT Team, points FROM top_8_1500m  -- 4 --
  UNION ALL
  SELECT Team, points FROM top_8_200m  -- 5 --
  UNION ALL
  SELECT Team, points FROM top_8_3000s  -- 6 --
  UNION ALL
  SELECT Team, points FROM top_8_400h  -- 7 --
  UNION ALL
  SELECT Team, points FROM top_8_400m  -- 8 --
  UNION ALL
  SELECT ï»¿Team, points FROM top_8_4x400 -- 9 --
  UNION ALL
  SELECT ï»¿Team, points FROM top_8_4x100 -- 10 --
  UNION ALL
  SELECT Team, points FROM top_8_5000m  -- 11--
  UNION ALL
  SELECT Team, points FROM top_8_800m  -- 12 --
  UNION ALL
  SELECT Team, points FROM top_8_decathlon  -- 13 --
  UNION ALL
  SELECT Team, points FROM top_8_hammer  -- 14 --
  UNION ALL
  SELECT Team, points FROM top_8_highjump  -- 15 --
  UNION ALL
  SELECT Team, points FROM top_8_longjump  -- 16 --
  UNION ALL
  SELECT Team, points FROM top_8_javelin  -- 17 --
  UNION ALL
  SELECT Team, points FROM top_8_polevault -- 18 --
  UNION ALL
  SELECT Team, points FROM top_8_shotput  -- 19 --
  UNION ALL
  SELECT Team, points FROM top_8_triplejump  -- 20 --
  UNION ALL
  SELECT Team, points FROM top_8_discus  -- 21 --
  ) AS CombinedTables
GROUP BY Team
ORDER BY TotalPoints DESC;


