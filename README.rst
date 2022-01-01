.. code-block:: python

   import datetime

   import coviddateutil

   print(coviddateutil.today())
   # => March 670, 2020

   print(
      coviddateutil.usingdate(
         datetime.datetime.now() - datetime.timedelta(days=1)
      )
   )
   # => March 669, 2020

   print(coviddateutil.usingdate(datetime.datetime(2019, 1, 15)))
   # => January 01, 2019
