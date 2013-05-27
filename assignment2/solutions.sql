/*	A. select.txt => σdocid=10398_txt_earn	*/
SELECT *
FROM docid
WHERE docid = '10398_txt_earn'

/* B. select_project.txt => πterm( σdocid=10398_txt_earn and count=1(frequency)) */
SELECT term
FROM Frequency
WHERE docid = '10398_txt_earn'
AND count = 1

/* C. union.txt => πterm( σdocid=10398_txt_earn and count=1(frequency)) */
SELECT term
FROM Frequency
WHERE docid = '10398_txt_earn'
AND count = 1

/* D. Number of documents containing the word “parliament” */
SELECT COUNT(*)
FROM Frequency
WHERE term = 'parliament'

/* E. All documents that have more than 300 total terms, including duplicate terms */
SELECT docid
FROM Frequency
GROUP BY docid
HAVING COUNT(docid) + SUM(count) > 300

/* F. Number of unique documents that contain both the word 'transactions' and the word 'world'. */
SELECT docid
FROM Frequency
WHERE term = 'transactions'
INTERSECT
SELECT docid
FROM Frequency
WHERE term = 'world'

