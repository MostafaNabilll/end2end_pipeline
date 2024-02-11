COPY INTO "DOGPIPELINE"."DOGS"."full_data"
FROM @s3_stage/denormalized_data.csv
FILE_FORMAT = (TYPE = 'CSV' FIELD_OPTIONALLY_ENCLOSED_BY = '"');