function generateExercise(tList::Vector, numList::Vector)
    str = ""
    for i in 1:length(tList)
        for j in 1:numList[i]
            str *= rand(tList[i]) * "      "
        end
    end
    return str;
end

function main(args)
    numAdj = args[2]
    numTechniques = args[3]
    numEx = args[1]
    adjectivesF = open("database/adj.txt");
    techniquesF = open("database/techniques.txt");

    adjectives = readlines(adjectivesF);
    techniques = readlines(techniquesF);
    typeList = [adjectives, techniques]

    println("")
    println("")
    for i in 1:numEx
        println(generateExercise(typeList, [numAdj, numTechniques]))
        println("")
    end
    println("")
    println("")
    return 1;
end

main([2, 1, 3])
