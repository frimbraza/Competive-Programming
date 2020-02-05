import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Abbreviate {

    private String sc = "\'";       // never used yet
    private String file;            // Original file
    private String [] wordList;

    // Main method
    public static void main(String[] args) throws IOException {
        Abbreviate test1 = new Abbreviate();
        String fileName = "test.txt";
        test1.readFile(fileName);
        test1.printFile();
        test1.abbrvte();

    }

    // Empty Constructor
    public Abbreviate() {
    }

    // Runs each word in wordList through the rules of abbreviation
    public void abbrvte() {
        stringToWords();
        // printWords();

        String abbrMessage = "";

        for (String word : wordList){
            String toPass = "";
            if(word.contains("\'")){                        // Might want to apply to all special characters, not just '
                String[] twoWord = word.split("\'");
                toPass += wordRule(twoWord[0]) + "\'" + wordRule(twoWord[1]);
            }
            else
                toPass = wordRule(word);
            abbrMessage += toPass + " ";
        }
        System.out.println(abbrMessage);
    }

    // Grabs the file from filename, and puts it in class variable
    public void readFile(String fileName) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader(fileName));
        try {
            StringBuilder sb = new StringBuilder();
            String line = br.readLine();

            while (line != null) {
                sb.append(line);
                sb.append("\n");
                line = br.readLine();
            }
            file =  sb.toString();
            return;
        } finally {
            br.close();
        }
    }

    // Turns a string into a list of words (seperates by white space)
    private void stringToWords() {
        wordList = file.split(" ");

        // Weird but there is a character at the end of the last word. Don't know how to fix nice, so here's a dirty way to do it.
        String lastWord = wordList[wordList.length - 1];
        lastWord = lastWord.substring(0, lastWord.length() - 1);
        wordList[wordList.length - 1] = lastWord;
    }

    // Just prints file for viewing
    public void printFile() {
        System.out.println(file);
    }

    // Just prints wordList for view
    public void printWords() {
        for (String word : wordList){
            System.out.println(word);
        }
    }

    // Removes vowels, but ignores ends of a word
    private String removeVowels(String word) {
        String wordCopy = word;
        String middleWord = word.substring(1, word.length() - 1);
        // System.out.println("middle:" + middleWord);
        middleWord =  middleWord.replaceAll("[aeiouAEIOU]", "");
        return wordCopy.charAt(0) + middleWord + wordCopy.charAt(wordCopy.length() - 1);
    }

    // Removes consecutive letters
    private String removeConsec(String word){
        String wordCopy = word;
        String newString = "";

        char prev = word.charAt(0);
        newString += prev;

        for (int i = 1; i < word.length(); ++i)
        {
            if(word.charAt(i) == prev){
            }
            else{
                newString += word.charAt(i);
            }
            prev = word.charAt(i);
        }
        return newString;
    }

    // Runs a word through all the rules
    private String wordRule(String word){
        String toPass = "";

        if(word.length() < 5)   // Don't change
        {
            toPass = word;
        }
        else                    // Abbreviate
        {
            toPass = removeVowels(word);
            toPass = removeConsec(toPass);
            // System.out.println(toPass);
        }
        return toPass;
    }
}