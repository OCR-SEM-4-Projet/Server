PGDMP     6                    z            OCR_Mini_project    12.9    12.9                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16590    OCR_Mini_project    DATABASE     �   CREATE DATABASE "OCR_Mini_project" WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'English_India.1252' LC_CTYPE = 'English_India.1252';
 "   DROP DATABASE "OCR_Mini_project";
                postgres    false            �            1259    16597    Admin    TABLE     !   CREATE TABLE public."Admin" (
);
    DROP TABLE public."Admin";
       public         heap    postgres    false            �            1259    16594    Result    TABLE     "   CREATE TABLE public."Result" (
);
    DROP TABLE public."Result";
       public         heap    postgres    false            �            1259    16591    User    TABLE         CREATE TABLE public."User" (
);
    DROP TABLE public."User";
       public         heap    postgres    false            �            1259    16600    result    TABLE     �   CREATE TABLE public.result (
    seat_no integer NOT NULL,
    name character varying(35),
    mcqs_marks double precision,
    q3_marks double precision,
    total_descriptive_marks double precision,
    total_marks double precision
);
    DROP TABLE public.result;
       public         heap    postgres    false            	          0    16597    Admin 
   TABLE DATA           !   COPY public."Admin"  FROM stdin;
    public          postgres    false    204   +
                 0    16594    Result 
   TABLE DATA           "   COPY public."Result"  FROM stdin;
    public          postgres    false    203   H
                 0    16591    User 
   TABLE DATA               COPY public."User"  FROM stdin;
    public          postgres    false    202   e
       
          0    16600    result 
   TABLE DATA           k   COPY public.result (seat_no, name, mcqs_marks, q3_marks, total_descriptive_marks, total_marks) FROM stdin;
    public          postgres    false    205   �
       	      x������ � �            x������ � �            x������ � �      
      x������ � �     