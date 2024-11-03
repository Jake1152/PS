SELECT st.student_id, st.student_name, su.subject_name, COUNT( ex.student_id ) as attended_exams
FROM Students st
CROSS JOIN subjects su 
LEFT JOIN 
(
    SELECT student_id, subject_name
    FROM Examinations
) AS ex
ON ex.student_id = st.student_id AND su.subject_name = ex.subject_name
GROUP BY st.student_id, su.subject_name
ORDER BY st.student_id, su.subject_name;
