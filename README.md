# Eurosender automatic balance checker
If you want your balance not to be to low, you run main.py every morning using windows scheduler. 
In main.py function sendCondition() you may change the default condition. Now its set to be so: if balance < 600 - send mail. if balance < 1000 and last time it was checked it was > 1000, then send mail
