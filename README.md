# INF 305 Database Management Systems 2. Spring 2022. Written by MIRUDI TEAM (Aru,Miras,Rufina) 

Cursors:
all_categories
CURSOR all_categories IS  SELECT id, category_id, category_name  FROM book_category;

2) all_bookings
CURSOR all_bookings   IS
     SELECT id, tracking_id, first_name,last_name,email, phone,room, adult, child, checkin_date, checkout_date, booking_date, hotel_id, user_id, price
 FROM book_booking;

3) CURSOR bookings_price_asc
   IS
     SELECT id, tracking_id, first_name,last_name,email, phone,room, adult, child, checkin_date, checkout_date, booking_date, hotel_id, user_id, price
     FROM book_booking order by price;
4) CURSOR bookings_price_desc
   IS
     SELECT id, tracking_id, first_name,last_name,email, phone,room, adult, child, checkin_date, checkout_date, booking_date, hotel_id, user_id, price
     FROM book_booking order by price desc;

5)  Барлык отель данный
set SERVEROUTPUT ON;+++++++++++++++++++
DECLARE 
 CURSOR cur_book IS SELECT id FROM book_booking;
   v_bname cur_book%ROWTYPE;
   v_name varchar2(255);
   v_address varchar2(255);
   v_city varchar2(255);
BEGIN 
OPEN cur_book;
LOOP 
  FETCH cur_book INTO v_bname;
   EXIT WHEN cur_book%NOTFOUND;
   for i in (Select city, name, address
      INTO v_name, v_address, v_city FROM book_hotel
     where v_bname.id = book_hotel.id) 
    LOOP
      DBMS_OUTPUT.PUT_LINE(i.name || ' ' || i.city || ' ' || i.address);
      END LOOP;
    END LOOP;
  CLOSE cur_book;
END;

6) Name and Surname бойынша
DECLARE 
CURSOR each_user IS 
SELECT first_name,last_name,email,phone,hotel_id
    FROM book_archive where first_name='Miras' and last_name='Tilegenov';
     v_name book_archive.first_name%TYPE;
     l_name book_archive.last_name%TYPE;
     v_email book_archive.email%TYPE;
     h_id book_archive.hotel_id%TYPE;
     v_phone book_archive.phone%TYPE;
BEGIN 
OPEN each_user;
  DBMS_OUTPUT.PUT_LINE('First_name || Last_name || Email || Phone || Hotel_id');
LOOP 
  FETCH each_user INTO v_name, l_name, v_email, h_id, v_phone;
  EXIT WHEN each_user%NOTFOUND;
  DBMS_OUTPUT.PUT_LINE(v_name ||'   '||l_name ||'   '|| v_email ||'   '|| h_id||'   '|| v_phone);
  END LOOP;
 CLOSE each_user;
 END;

7)Отель айдига байланысты данный шыгарады
DECLARE
   CURSOR booking_hotel
   IS
      SELECT first_name,last_name,email,phone 
      FROM book_booking WHERE hotel_id= 4;
      v_name book_booking.first_name%TYPE;
      l_name book_booking.last_name%TYPE;
      v_email book_booking.email%TYPE;
      v_phone book_booking.phone%TYPE;
BEGIN 
   FOR i IN booking_hotel
   LOOP
      DBMS_OUTPUT.put_line (i.FIRST_NAME ||' '|| I.LAST_NAME ||' '|| I.EMAIL ||' '|| I.PHONE);
   END LOOP;
END;




Procedures:
айди бойынша отель шығаратын
1)CREATE OR REPLACE procedure all_hotels(id_num number)
IS
v_id  book_hotel.id%type;
v_city  book_hotel.city%type;
v_name  book_hotel.name%type;
v_address  book_hotel.address%type;
v_overview  book_hotel.overview%type;
v_highlight   book_hotel.highlight%type;
v_room_types  book_hotel.room_types%type;
v_rating  book_hotel.rating%type;
v_price  book_hotel.price%type;
CURSOR all_hotels IS
SELECT id, city, name,address, overview,highlight, room_types, rating, price FROM book_hotel where book_hotel.id=id_num;
BEGIN
OPEN all_hotels;
FETCH all_hotels INTO v_id, v_city, v_name, v_address, v_overview, v_highlight, v_room_types, v_rating, v_price;
      DBMS_OUTPUT.PUT_LINE(v_id|| ' - ' || v_city  ||' - '  ||v_name);
CLOSE all_hotels;
END;

begin
all_hotels(1);
end;


Әр қаладағы хотел саны+++++++

set SERVEROUTPUT ON;
create or replace procedure hotel_count
is 
 countter NUMBER;
 hotel_city varchar2(255);
Begin
 for i in (SELECT city, COUNT(*) as cnt into hotel_city,countter FROM book_hotel
    GROUP BY book_hotel.city ORDER BY book_hotel.city) LOOP
   DBMS_OUTPUT.put_line( i.city || ' ' ||  i.cnt);
END LOOP;
END;
проверка
begin
hotel_count;
end;

Отели больше какой-то суммы
set SERVEROUTPUT ON;
create or replace procedure price_compare(p_price NUMBER)
is 
 h_name varchar2(255);
 h_price NUMBER;
Begin
 for i in (SELECT name, price into h_name,h_price FROM book_hotel where book_hotel.price>=p_price) 
LOOP
   DBMS_OUTPUT.put_line( i.name || ' ' ||  i.price);
END LOOP;
END;

begin
price_compare(60000);
end;

Дата енгізесің чек ин уақыт адамдар списогын  шығарып беред
set SERVEROUTPUT ON;
create or replace procedure checktime(year_d VARCHAR2)
is 
 h_name varchar2(255);
 f_name varchar2(255);
 l_name varchar2(255);
 p_number number;
Begin
 DBMS_OUTPUT.put_line(year_d);
 for i in (SELECT name,first_name, last_name, phone into h_name,f_name, l_name, p_number FROM book_hotel JOIN book_booking 
           ON book_booking.hotel_id=book_hotel.id where year_d=book_booking.checkin_date)
LOOP
   DBMS_OUTPUT.put_line( i.name || ' ' ||  i.first_name || ' ' ||  i.last_name || ' ' ||  i.phone);
END LOOP;
END;

begin
checktime('May 06, 2022');
end;
5)Дата енгізесің чек out уақыт адамдар списогын  шығарып беред

set SERVEROUTPUT ON;
create or replace procedure checktime(year_d VARCHAR2)
is 
 h_name varchar2(255);
 f_name varchar2(255);
 l_name varchar2(255);
 p_number number;
Begin
 DBMS_OUTPUT.put_line(year_d);
 for i in (SELECT name,first_name, last_name, phone into h_name,f_name, l_name, p_number FROM book_hotel JOIN book_booking 
           ON book_booking.hotel_id=book_hotel.id where year_d=book_booking.checkout_date)
LOOP
   DBMS_OUTPUT.put_line( i.name || ' ' ||  i.first_name || ' ' ||  i.last_name || ' ' ||  i.phone);
END LOOP;
END;

begin
checktime('May 26, 2022');
end;

6)Tracking_id бойынша
create or replace FUNCTION track_f(tracking_id IN VARCHAR2) 
   RETURN VARCHAR2
   IS user_details VARCHAR2(130);
   cursor track_c is 
   SELECT 'Name:'||book_booking.first_name||'; Last name-'|| book_booking.last_name||',Checkin date:'||book_booking.Checkin_date||'; Checkout date:'||book_booking.Checkout_date 
    FROM book_booking;
   BEGIN 
      open track_c;
      fetch track_c into user_details;
      DBMS_OUTPUT.PUT_LINE('Information ' || user_details);
      close track_c;
      RETURN(user_details); 
END track_f;

DECLARE
  track_ex VARCHAR2(130);
begin
  track_ex:=track_f('MT1652173384');
end;



Transactions:
1)SET TRANSACTION READ WRITE;

DECLARE
BEGIN
   SAVEPOINT do_insert;
   INSERT INTO book_hotel(city, name, address, overview, highlight, room_types, rating, price, imgurls)
   VALUES( 'Aktobe', 'Diyaru', 'Zhubanov 47', 'hello', '#wifi, #park', 'Luxe', '5', '150000', '/media-cdn.tripadvisor.com/media/photo-s/16/1a/ea/54/hotel-presidente-4s.jpg');
EXCEPTION
   WHEN DUP_VAL_ON_INDEX THEN
      ROLLBACK TO do_insert;
      DBMS_OUTPUT.PUT_LINE('Insert has been rolled back');
END;
commit;

SET TRANSACTION READ WRITE;
UPDATE BOOK_HOTEL
SET NAME='Diyaru'
WHERE NAME='MIRAS';
commit;


SET TRANSACTION READ WRITE;
Delete from BOOK_HOTEL
WHERE NAME='Diyaru';
commit;





TRIGGERS
АРХИВ
create or replace trigger to_book_archive 
   before delete on book_booking
   for each row
   declare 
     variable_name book_booking%ROWTYPE;
   begin
     insert into book_archive(id, tracking_id,first_name,last_name,email,phone,room,adult,child, checkin_date, checkout_date,booking_date,price,hotel_id, user_id)
     values(:old.id,:old.tracking_id,:old.first_name,:old.last_name, :old.email, :old.phone, :old.room, :old.adult, :old.child, :old.checkin_date, :old.checkout_date, :old.booking_date, :old.price, :old.hotel_id, :old.user_id);
   end;

  delete from book_booking where id=2;

2)User Archive before delete
create or replace trigger delete_user
  before delete ON book_user
     FOR EACH ROW
begin
       Insert into book_userarchive (id,user_id,username, first_name, last_name, phone) 
       values ('1', :old.id,:old.username, :old.first_name, :old.last_name, :old.phone);
end;

delete from book_user where id=21;

3)User archive after update
create or replace trigger update_user
  AFTER UPDATE ON book_user
     FOR EACH ROW
begin
       Insert into book_userarchive (id,user_id,username, first_name, last_name, phone) 
       values ('3', :old.id,:old.username, :old.first_name, :old.last_name, :old.phone);
end;

update book_user
set first_name='Miras'
where first_name='Aru'





