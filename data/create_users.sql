CREATE TABLE users (
                       email STRING PRIMARY KEY,
                       last_name STRING,
                       first_name STRING,
                       phone_numbers STRING ARRAY
);
CREATE TABLE rides (
                       id UUID PRIMARY KEY,
                       vehicle_id UUID REFERENCES vehicles (id),
                       user_email STRING REFERENCES users (email),
                       start_ts TIMESTAMP,
                       end_ts TIMESTAMP
);
