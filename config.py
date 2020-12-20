# This file should be hidden, to not expose sensitive data
import os

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# database local conenction params
database_params = {
    "username": "root",
    "password": "",
    "db_name": "casting_agency",
    "dialect": "postgresql"
}

# auth0 token that are used for unit_test

auth0_tokens = {
    "casting_assistant": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ilg0a0dmZDFUV1M5UXNOX0JhOWFTWSJ9.eyJpc3MiOiJodHRwczovL21hdGVmLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWViY2Q1ODYwYjYyOTAwMTM4NmMyMTIiLCJhdWQiOiJteWFwcCIsImlhdCI6MTU5MjUxMzg5OCwiZXhwIjoxNTkyNjAwMjk4LCJhenAiOiJjS3lMY1ZDRGtMRHNJeVVhdFZHbFpqN2xQNXhqN0ZiZCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.Ll6uCWa96cM9dIXm-KoIwJwIpkb06zn8YMvJHMVB6JCYcA9k9Dg2n_PZKEhnCXsxV1MCQmTI3B5Bn3idCXo9Y1pM2u9SxPm1WW-3-p2K07dHtqhw67jTM0DtCBUgCSqK-x0boBedxtQiABJgvKislYeseJyWkbOVU0tiUQpOX1WlZJ--kSSSTLOafO3idhFdfo02X3-UFJJVSRyXbrwbRFx0WaIkOYq1cEA1xt_tg5kechdoblgTMGYzVylUa0vIMS_bqbToukKxkUFxXK2OfFnFvhkWdoaonpoae1DZa_5TonoNktQzrWoPFwnPseE_QDDzrp3nSFYCGXri9XdtdQ",
    "casting_director": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ilg0a0dmZDFUV1M5UXNOX0JhOWFTWSJ9.eyJpc3MiOiJodHRwczovL21hdGVmLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWViY2Q3YjNiOWQ2NjAwMTkxYWYwN2QiLCJhdWQiOiJteWFwcCIsImlhdCI6MTU5MjUxNDE1NSwiZXhwIjoxNTkyNjAwNTU1LCJhenAiOiJjS3lMY1ZDRGtMRHNJeVVhdFZHbFpqN2xQNXhqN0ZiZCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiY3JlYXRlOmFjdG9ycyIsImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInVwZGF0ZTphY3RvcnMiLCJ1cGRhdGU6bW92aWVzIl19.e6cgp-zo5VMETTlfHCeMCYnjCH8G8KEvaPP50q3D2S5QE6ro3SO4cxoLrzqbOu4CioA4GLlU0wvGHTyYgZI18cpQpB4TXZyWpPGUvsrnBRtEmRvZSQgQJPsQqkaU2Hzx9jKI5v8oOteEhn5H5A3I9DKafHyp0cYtsp0OK1wgExR4LYe5s4YwXM8OAGlk7Z3oORQ5tzPbFVbQipNv2IYuCjnB0HDtfMjkTw-sqKtk8J_1UNlhEUWHvPuR-vAnpdkthC8gt1Z1KpYGD_g_itOLuOjmAcvmhaX3EvyMeQCyb_MNbJLZ0837DiGMDjsMYaXmyzvrH8nM9bSgK8nJc9ervw",
    "executive_producer": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ilg0a0dmZDFUV1M5UXNOX0JhOWFTWSJ9.eyJpc3MiOiJodHRwczovL21hdGVmLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWViY2RiMTU5NGIyMTAwMTM2NWU1N2QiLCJhdWQiOiJteWFwcCIsImlhdCI6MTU5MjUxMzk4MSwiZXhwIjoxNTkyNjAwMzgxLCJhenAiOiJjS3lMY1ZDRGtMRHNJeVVhdFZHbFpqN2xQNXhqN0ZiZCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiY3JlYXRlOmFjdG9ycyIsImNyZWF0ZTptb3ZpZXMiLCJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwidXBkYXRlOmFjdG9ycyIsInVwZGF0ZTptb3ZpZXMiXX0.KmuEoYxRornotkbm9z0m2O-eGfgoPFO13HyayHaeo8_hZwZbtw-TvqAeCabwHfWoTG8A68HvZyBz8aBKGc48NGNXasvbDfJvDD1QMLseRG-DuWoAOEWQzuWD3JLw9ivctBNzNZ7jWd3IalZsXulEIUb9h5P_iaaOT7LoAS1K-pJi-A8V_Wl1jsi9-eLIKrIEwIh2QEoqpV72epD2BK6qsH2gB5UftfabMdcJ51RiZIPunsYM9tZfak4CB4qmxuqfGPENrz_MZ1SNj9NXEHIs8Zzs_Ja8RZ3YySGM_z6-unjJpTjJtjfPFf00SgsRyaFNdDGaKZSdjoDWB0P5k4BeNA"
}
