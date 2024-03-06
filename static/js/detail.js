//get argue form template
guide = JSON.parse(document.getElementById("dataTrans").dataset.iteminfo.replaceAll("\'","\""))
console.log(guide)

//translate token into Quote
guide.CommonName = guide.CommonName.replaceAll("_tokeForSingleQuote_","'")
guide.CommonName = guide.CommonName.replaceAll("_tokeForDoubleQuote_",'"')

guide.ScientificName = guide.ScientificName.replaceAll("_tokeForSingleQuote_","'")
guide.ScientificName = guide.ScientificName.replaceAll("_tokeForDoubleQuote_",'"')

guide.KeyCharacteristics = guide.KeyCharacteristics.replaceAll("_tokeForSingleQuote_","'")
guide.KeyCharacteristics = guide.KeyCharacteristics.replaceAll("_tokeForDoubleQuote_",'"')

guide.BiologyDescription = guide.BiologyDescription.replaceAll("_tokeForSingleQuote_","'")
guide.BiologyDescription = guide.BiologyDescription.replaceAll("_tokeForDoubleQuote_",'"')

guide.Impacts = guide.Impacts.replaceAll("_tokeForSingleQuote_","'")
guide.Impacts = guide.Impacts.replaceAll("_tokeForDoubleQuote_",'"')

console.log(guide)


document.getElementById("commonName").innerHTML = guide.CommonName
document.getElementById("scientificName").innerHTML = guide.ScientificName

document.getElementById("keyCharacteristics").innerHTML = guide.KeyCharacteristics
document.getElementById("biologyDescription").innerHTML = guide.BiologyDescription
document.getElementById("impacts").innerHTML = guide.Impacts

document.getElementById("anothercommonName").innerHTML = guide.CommonName
