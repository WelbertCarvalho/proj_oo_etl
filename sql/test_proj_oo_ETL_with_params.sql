select 
    * 
from 
    datalake.cotacao_moedas 
where 
    created_date >= %s 
    and created_date <= %s