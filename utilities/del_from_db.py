import psycopg2


def delete_from_vacancy_resume():
    con = psycopg2.connect(host='localhost',
                           database='rabotyNET',
                           user='postgres',
                           password='postgres')
    cur = con.cursor()

    cur.execute('select vacancy_id, resume_id from vacancy_resume')

    rows = cur.fetchall()

    if rows:
        cur.execute('delete from vacancy_resume')
        con.commit()
        cur.close()
        con.close()
    else:
        cur.close()
        con.close()


def delete_from_claim():
    con = psycopg2.connect(host='localhost',
                           database='rabotyNET',
                           user='postgres',
                           password='postgres')
    cur = con.cursor()

    cur.execute('select claim_id, description from claim')

    rows = cur.fetchall()

    if rows:
        cur.execute('delete from claim')
        con.commit()
        cur.close()
        con.close()
    else:
        cur.close()
        con.close()
