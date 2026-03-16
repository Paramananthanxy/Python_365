#9.12 Multiple Modules callling in same file 
from Admin import Admin

ad = Admin("Jammie","Lanister",8,age='10')
ad.describe_user()
ad.Privilege.show_privileges()