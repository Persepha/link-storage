SELECT auth_user.email, 
       ranked_links.count_links,
       ranked_links.website,
       ranked_links.book,
       ranked_links.article,
       ranked_links.music,
       ranked_links.video
FROM auth_user
JOIN (
    SELECT user_id, 
           COUNT(*) AS count_links,
           COUNT(*) FILTER (WHERE link_type = 'website') AS website,
           COUNT(*) FILTER (WHERE link_type = 'book') AS book,
           COUNT(*) FILTER (WHERE link_type = 'article') AS article,
           COUNT(*) FILTER (WHERE link_type = 'music') AS music,
           COUNT(*) FILTER (WHERE link_type = 'video') AS video
    FROM storage_link
    GROUP BY user_id
) AS ranked_links ON auth_user.id = ranked_links.user_id
ORDER BY ranked_links.count_links DESC, auth_user.date_joined ASC
LIMIT 10;