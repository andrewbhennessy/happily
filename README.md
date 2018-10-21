# happily
An experimental emotional monitoring project utilizing distributed cameras, DynamoDB, Lambda, API Gateway, Rekognition, and Webcam.js

**Thanks for checking us out!**

## Inspiration
NCR mobile kiosk solutions. How can we further brand intelligence through analyzing customer behavior through video? We pivoted last minute to leverage the powerful sentimental capabilities of the Amazon Rekognition pipeline.

## What it does
As a result---the ability to candidly collect a timeline of peoples "emotions"!

## How we built it
Low overhead web app that sends photos through APIgateway to Lambda function that sends data in and out of Rekognition pipeline. We utilized the collections capability to track every interaction unique people have and store everything in DynamoDB. We also utilized the instant SDK creation capabilities of Amazon APIgateway for javascript.

## Challenges we ran into
Fragmented situation between frontend and backend. We spent most of our time ironing out those issues instead of innovating. The third party APIs offered to us, that we wanted to use, were just too much---not enough time! 

## Accomplishments that we're proud of
We made it past the finish line with an MVP, which for a hackathon project has some pretty cool potential. We are excited to see our group members go on there separate ways and keep working on the project. We are proud of working with the special components of the Rekognition API that extracts facial feature data into a feature vector that is anonymous enough to be **HIPPA** compliant. 

## What we learned
Planning is everything, we spent a lot of time doing that and we avoided many common issues. Namely, we did not bite off more than we could chew which led us to a pretty cool idea that has future potential. The **ONE** morale booster we needed this weekend :\

## What's next for happily
Hardware integration---making it easier to collect more data. Working harder to leverage the data we never really had a chance to manipulate. Finding a community partner that would have a vested interest in working with the idea. 
