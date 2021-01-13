fs.readFile('./tweets.json', 'utf8', (err, jsonString) => {
    if (err) {
        console.log("Error reading file from disk:", err)
        return
    }
    try {
        const tweets = JSON.parse(jsonString)
        console.log("First tweet is:", tweets.tweet_text) //
} catch(err) {
        console.log('Error parsing JSON string:', err)
    }
})
    
    