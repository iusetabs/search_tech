package main;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.util.ArrayList;

import org.apache.commons.io.FileUtils;

import summarizer.Weighter;
import tokenizer.PageStructure;
import tokenizer.Structurer;

public class SerializingWeights {

	/**
	 * @param args
	 * @throws IOException 
	 */
	public static void main(String[] args) throws IOException {
		String text = FileUtils.readFileToString(new File("C:\\Users\\Procheta\\Desktop\\qrel_user_15.txt"), "UTF-8");
		Structurer structurer = new Structurer();
		PageStructure structure = structurer.getStructure(text);	
		
		Weighter weighter = new Weighter();
		ArrayList<Double[]> weights = new ArrayList<Double[]>();
		weighter.setStructure(structure);
		weighter.calculateWeights(weights);
		
		try {
			FileOutputStream fileOut = new FileOutputStream(new File("C:\\Users\\Procheta\\Desktop/test"));
			ObjectOutputStream out = new ObjectOutputStream(fileOut);
			out.writeObject(weights);
			out.close();
			fileOut.close();
		} catch(IOException e) {
			e.printStackTrace();
		}
	}

}
