select 
    * 
from 
    sakila.film 
where 
    last_update >= %s 
    and last_update <= %s