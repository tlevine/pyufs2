// http://microformat2-node.jit.su/h-product.html

{
    "items": [{
        "type": ["h-product"],
        "properties": {
            "name": ["Raspberry Pi"],
            "photo": ["http://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/RaspberryPi.jpg/320px-RaspberryPi.jpg"],  
            "description": ["The Raspberry Pi is a credit-card sized computer that plugs into your TV and a keyboard. It’s a capable little PC which can be used for many of the things that your desktop PC does, like spreadsheets, word-processing and games. It also plays high-definition video. We want to see it being used by kids all over the world to learn programming."],
            "url": ["http://www.raspberrypi.org/"],
            "price": ["£29.95"],
            "review": [{
                "value": "9.2 out of 10 based on 178 reviews",
                "type": ["h-review-aggregate"],
                "properties": {
                    "rating": [{
                        "value": "9.2 out of 10 based on 178 reviews",
                        "type": ["h-rating"],
                        "properties": {
                            "average": ["9.2"],
                            "best": ["10"],
                            "count": ["178"],
                            "name": ["9.2 out of 10 based on 178 reviews"]
                        }
                    }], 
                    "name": ["9.2 out of 10 based on 178 reviews"]
                }
            }],
            "category": ["Computer","Education"],
            "brand": [{
                "value": "From: The Raspberry Pi Foundation - Cambridge UK",
                "type": ["h-card"],
                "properties": {
                    "name": ["The Raspberry Pi Foundation"], 
                    "org": ["The Raspberry Pi Foundation"],
                    "locality": ["Cambridge"],
                    "country-name": ["UK"]
                }
            }]
        }
    }]
}
