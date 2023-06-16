-- language: sql
--
-- PostgreSQL database dump
--

-- Dumped from database version 12.15 (Ubuntu 12.15-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.15 (Ubuntu 12.15-0ubuntu0.20.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer,
    name character varying(255),
    age integer
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, name, age) FROM stdin;
0	Enzo Pires	54
1	Dr. Leandro Castro	61
2	Maitê Fernandes	48
3	Maria Luiza Rezende	54
4	Evelyn Oliveira	31
5	Sr. João Gabriel Silveira	31
6	Sra. Ana Laura Gonçalves	64
7	Bruna Correia	24
8	Marcela Carvalho	65
9	Enzo Barros	63
\.


--
-- PostgreSQL database dump complete
--

