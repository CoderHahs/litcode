-- A telecommunications company charges its customers for both incoming and outgoing calls based on the number of call
-- units. A call unit is an internal representation of the amount that the company should charge its customers. It maintains
-- the records of all the calls made on its network in table, call_record, storing information such as incoming number,
-- outgoing number, duration of the call and the date on which the call was made. Write a query to calculate the bills of all
-- the customers for the month of May, 2018. It should only include customers who have made or received any calls in the
-- given period. The order of output does not matter. The result should be in the following format: name phone_number call units

-- The company calculates charges as follows:
-- • For incoming calls, a standard charge of 1 call unit/second is levied. Example: For an incoming call of 2 minutes 30 seconds,
-- 150 call units will be charged.
-- • For outgoing calls, a fixed charge of 500call units is charged for the first 2 minutes ofa call, then 2call units/second is levied
-- against the remainder. Example: For a call of 3 minutes, 620 call units will be charged (500 + 60*2).

-- Schema

-- There are 2 tables: customer detail and call record

-- customer_detail:
-- id (INTEGER) - this is the customer's id. It is the primary key. 
-- name (STRING) - Customer's name
-- phone_number (STRING) - Customer's phone number

-- call_record:
-- id (integer) - this is the record id
-- incoming_number (STRING) - incoming number or the call recipient's number
-- outgoing_number (STRING) - outgoing number or the call dialer's number
-- duration (INTEGER) - call duration in seconds
-- dialed_on (DATE) - Call date

with may_records_trunc as (
    select name, phone_number, IF(r.incoming_number = c.phone_number, 'I', 'O') as io, duration
    from call_record as r
    join customer_detail as c
    on r.incoming_number = c.phone_number
    or r.outgoing_number = c.phone_number
    where dialed_on >= '2018-05-01'
    and dialed_on <= '2018-05-31'
),
calculated_per_call as (
    select phone_number, io, duration, 
    case
        when io = 'I' then duration
        when io = 'O' then IF(duration > 120, 500+2*(duration-120), 500)
    end as call_unit
    from may_records_trunc
),
aggregated as (
select phone_number, SUM(call_unit) as cu
from calculated_per_call
group by phone_number
)
select name, c.phone_number, cu
from customer_detail as c
join aggregated as a
on c.phone_number = a.phone_number;
