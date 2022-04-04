PGDMP                         z            OCR    12.9    12.9                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16603    OCR    DATABASE     �   CREATE DATABASE "OCR" WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'English_India.1252' LC_CTYPE = 'English_India.1252';
    DROP DATABASE "OCR";
                postgres    false            �            1259    16606    admin    TABLE     �   CREATE TABLE public.admin (
    id integer NOT NULL,
    username character varying,
    email character varying,
    password character varying
);
    DROP TABLE public.admin;
       public         heap    postgres    false            �            1259    16604    admin_id_seq    SEQUENCE     �   CREATE SEQUENCE public.admin_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.admin_id_seq;
       public          postgres    false    203                       0    0    admin_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.admin_id_seq OWNED BY public.admin.id;
          public          postgres    false    202            �            1259    16621    result    TABLE     3  CREATE TABLE public.result (
    id integer NOT NULL,
    seat_no character varying,
    name character varying,
    "Mcq_marks" integer NOT NULL,
    q2_marks integer NOT NULL,
    q3_marks integer NOT NULL,
    "Tot_des_marks" integer NOT NULL,
    "Tot_marks" integer NOT NULL,
    conform_by integer
);
    DROP TABLE public.result;
       public         heap    postgres    false            �            1259    16619    result_id_seq    SEQUENCE     �   CREATE SEQUENCE public.result_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE public.result_id_seq;
       public          postgres    false    205                       0    0    result_id_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE public.result_id_seq OWNED BY public.result.id;
          public          postgres    false    204            �
           2604    16609    admin id    DEFAULT     d   ALTER TABLE ONLY public.admin ALTER COLUMN id SET DEFAULT nextval('public.admin_id_seq'::regclass);
 7   ALTER TABLE public.admin ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    203    202    203            �
           2604    16624 	   result id    DEFAULT     f   ALTER TABLE ONLY public.result ALTER COLUMN id SET DEFAULT nextval('public.result_id_seq'::regclass);
 8   ALTER TABLE public.result ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    205    204    205                      0    16606    admin 
   TABLE DATA           >   COPY public.admin (id, username, email, password) FROM stdin;
    public          postgres    false    203   N                 0    16621    result 
   TABLE DATA           ~   COPY public.result (id, seat_no, name, "Mcq_marks", q2_marks, q3_marks, "Tot_des_marks", "Tot_marks", conform_by) FROM stdin;
    public          postgres    false    205   k                  0    0    admin_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.admin_id_seq', 1, false);
          public          postgres    false    202                       0    0    result_id_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public.result_id_seq', 1, false);
          public          postgres    false    204            �
           2606    16616    admin admin_email_key 
   CONSTRAINT     Q   ALTER TABLE ONLY public.admin
    ADD CONSTRAINT admin_email_key UNIQUE (email);
 ?   ALTER TABLE ONLY public.admin DROP CONSTRAINT admin_email_key;
       public            postgres    false    203            �
           2606    16618    admin admin_password_key 
   CONSTRAINT     W   ALTER TABLE ONLY public.admin
    ADD CONSTRAINT admin_password_key UNIQUE (password);
 B   ALTER TABLE ONLY public.admin DROP CONSTRAINT admin_password_key;
       public            postgres    false    203            �
           2606    16614    admin admin_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.admin
    ADD CONSTRAINT admin_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.admin DROP CONSTRAINT admin_pkey;
       public            postgres    false    203            �
           2606    16629    result result_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.result
    ADD CONSTRAINT result_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.result DROP CONSTRAINT result_pkey;
       public            postgres    false    205            �
           2606    16630    result result_conform_by_fkey    FK CONSTRAINT        ALTER TABLE ONLY public.result
    ADD CONSTRAINT result_conform_by_fkey FOREIGN KEY (conform_by) REFERENCES public.admin(id);
 G   ALTER TABLE ONLY public.result DROP CONSTRAINT result_conform_by_fkey;
       public          postgres    false    203    205    2702                  x������ � �            x������ � �     