package main;

import summarizer.Aggregator;
import summarizer.Summarizer;
import summarizer.Weighter;
import tokenizer.Structurer;

import java.io.File;

import org.apache.commons.io.FileUtils;


public class Test {
	public static void main(String [] args) throws Exception {
		String text = FileUtils.readFileToString(new File(args[0]));
		Structurer structurer = new Structurer();
		Weighter weighter = new Weighter();
		Aggregator aggregator = new Aggregator();		
		Summarizer summarizer = new Summarizer(structurer, weighter, aggregator);
		summarizer.setNumSentences(Integer.parseInt(args[1]));
		String summary = summarizer.summarize(text);
		System.out.println("Summary:  "+summary);
	}
}
