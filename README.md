#Basics of jsonpath, jq and yq
**Table of Contents**


[TOC]
##Table Representation
Category  | Author | Title | Cost
------------- | -------------| ------------- | -------------
Reference  | Nigel Rees | Sayings of the Century | 9.95$
Fiction | Herman Melville | Moby Dick | 8.95$
Fiction | J.R.R. Tolkien | The Lord of the Rings | 10.0$
Education | R S Agarwal | Arithmetic and Reasoning | 11.99$
Mythological | Amish Tripati | Secreats of Nagas | 5.99$

##JSON Representation 

	{
    "store": {
      "book": [
        {
          "category": "reference",
          "author": "Nigel Rees",
          "title": "Sayings of the Century",
          "price": 9.95$
        },
        {
          "category": "fiction",
          "author": "Herman Melville",
          "title": "Moby Dick",
          "price": 8.95$
        },
        {
          "category": "fiction",
          "author": "J.R.R. Tolkien",
          "title": "The Lord of the Rings",
          "price": 10.0$
        },
		{
          "category": "Education",
          "author": "RS Agarwal",
          "title": "Arithmetic and Reasoning",
          "price": 11.99$
        },
		{
          "category": "Mythological",
          "author": "Amish Thripati",
          "title": "Secreats of Nagas",
          "price": 5.99$
        }
      ]
  	}
	}


## YAML Representation 
	store:
  		book:
			- category: reference
			  author: Nigel Rees
			  title: Sayings of the Century
			  price: 9.95$
			- category: fiction
			  author: Herman Melville
			  title: Moby Dick
			  price: 8.95$
			- category: fiction
			  author: J.R.R. Tolkien
			  title: The Lord of the Rings
			  price: 10.0$
			- category: Education
			  author: RS Agarwal
			  title: Arithmetic and Reasoning
			  price: 11.99$
			- category: Mythological
			  author: Amish Thripati
			  title: Secreats of Nagas
			  price: 5.99$
