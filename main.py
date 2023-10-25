import sys
sys.path.append('.')
import nav
import text
import savedb
import res

response=nav.getData('https://www.weibo.com/ajax/feed/allGroups')

navs=nav.parse_json(response.json())
texts=text.get_data(navs)
for i in texts:
    savedb.save(i)

res.db_connection.commit()
res.db_connection.close()



