
# Introduction
There is a wide disparity in online knowledge articles for Hindi Wikipedia pages and English Wikipedia pages. For example, there around 6M articles in English v/s 150K in Hindi. This leads to lack of access to comprehensive content for native language speakers.Currently, Wikipedia articles are manually translated from English to Hindi which is a labor intensive process. One possible existing method is direct translation by LLMs, but this struggles in effective generation due to token limitations. 

We aim to leverage Wikidata as a foundational knowledge base for article generation as translating structured data easier than translating longer articles. We aim to combine Retrieval-Augmented Generation (RAG) with structured knowledge retrieval to generate Wikipedia articles in Indian languages. Broadly, we will follow the below steps: 
1. Create and store templates using generated & existing articles.
2. Using occupation specific templates (eg: Scientists, Business Person) ensuring consistency in format and tone across entities of an occupation.
3. Enables article generation for new entities with minimal adjustments


# Overview of Project Structure
| Directory      | SubFolder             |                     Description                   |
|----------------|-----------------------|---------------------------------------------------|
| main           | json_conversion       | Conversion of English JSON Files to Hindi         |
| main           | template_generation   | Generatation of Hindi Template Sentences          |
| main           | article_generation    | Article Generation both With and Without Template |
| evaluation     | -                     | Converted JSON & Article Generation Evaluation    |

# Setup Details
1: Install the dependencies using the requirements.txt
```
pip install -r requirements.txt
```

2: Make sure you have access to the Llama-3.1 70 B model on Hugging Face[1], ChatOpenAI API[2] and Chat Open AI embeddings[2]. You will need to add the user tokens of these in the necessary files under the folder json_conversion, template_generation and evaluation respectively.

3: We ran this on the Georgia Tech Pace Clusters[3] on NVIDIA A100 or NVIDIA H100 GPUs depending on availability in the cluster.

4: We use the 4 Bit Quantized version from Unsloth[4, 5] for the Llama 3.1 70 B model taking into account the overall resource availabilities. It took around 40G space to load this model on the GPU.

# References
1. https://huggingface.co/meta-llama/Llama-3.1-70B
2. https://openai.com/api/
3. https://pace.gatech.edu/
4. https://huggingface.co/unsloth/Meta-Llama-3.1-70B-bnb-4bit
5. https://colab.research.google.com/drive/1Ys44kVvmeZtnICzWz0xgpRnrIOjZAuxp?usp=sharing
6. Achiam, J., Adler, S., Agarwal, S., Ahmad, L., Akkaya, I., Aleman, F. L., Almeida, D., Altenschmidt, J., Altman, S., Anadkat, S., et al. (2023). GPT-4 technical report. arXiv preprint arXiv:2303.08774.
7. Agarwal, A., & Mamidi, R. (2023). Automatically generating Hindi Wikipedia pages using Wikidata as a knowledge graph: A domain-specific template sentences approach. In Proceedings of the 14th International 8. Conference on Recent Advances in Natural Language Processing (pp. 11–21). Varna, Bulgaria: INCOMA Ltd., Shoumen, Bulgaria.
8. Axelsson, A., & Skantze, G. (2023). Using large language models for zero-shot natural language generation from knowledge graphs. arXiv preprint arXiv:2307.07312.
9. Cai, D., Wang, Y., Li, H., Lam, W., & Liu, L. (2021). Neural machine translation with monolingual translation memory. In Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers) (pp. 7307–7318). Association for Computational Linguistics.
10. Chase, H. (2022). Langchain. Retrieved from [Langchain citation].
11. Chen, M., Lu, X., Xu, T., Li, Y., Zhou, J., Dou, D., & Xiong, H. (2023). Towards table-to-text generation with pretrained language model: A table structure understanding and text deliberating approach. arXiv preprint arXiv:2301.02071.
12. Douze, M., Guzhva, A., Deng, C., Johnson, J., Szilvasy, G., Mazaré, P.-E., Lomeli, M., Hosseini, L., & Jégou, H. (2024). The FAISS library.
13. Dubey, A., Jauhri, A., Pandey, A., Kadian, A., Al-Dahle, A., Letman, A., Mathur, A., Schelten, A., Yang, A., Fan, A., et al. (2024). The LLaMA 3 herd of models. arXiv preprint arXiv:2407.21783.
14. Es, S., James, J., Anke, L. E., & Schockaert, S. (2024). RAGAs: Automated evaluation of retrieval augmented generation. In Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics: System Demonstrations (pp. 150–158). St. Julians, Malta: Association for Computational Linguistics.
15. Jiang, A. Q., Sablayrolles, A., Mensch, A., Bamford, C., Chaplot, D. S., Casas, D. de las, Bressand, F., Lengyel, G., Lample, G., Saulnier, L., Renard Lavaud, L., Lachaux, M.-A., Stock, P., Le Scao, T., Lavril, T., Wang, T., Lacroix, T., & El Sayed, W. (2023). Mistral 7B. arXiv preprint arXiv:2310.06825.
16. Lai, V. D., Ngo, N. T., Ben Veyseh, A. P., Man, H., Dernoncourt, F., Bui, T., & Nguyen, T. H. (2023). ChatGPT beyond English: Towards a comprehensive evaluation of large language models in multilingual learning. arXiv preprint arXiv:2304.05613.
17. Lin, C.-Y. (2004). ROUGE: A package for automatic evaluation of summaries. Retrieved from [https://aclanthology.org/W04-1013.pdf].
18. Liu, Y., Iter, D., Xu, Y., Wang, S., Xu, R., & Zhu, C. (2023). G-Eval: NLG evaluation using GPT-4 with better human alignment. arXiv preprint arXiv:2303.16634.
19. Marcheggiani, D., & Perez-Beltrachini, L. (2018). Deep graph convolutional encoders for structured data to text generation. In Proceedings of the 11th International Conference on Natural Language Generation (pp. 1–9). Tilburg University, The Netherlands: Association for Computational Linguistics.
20. Moussallem, D., Gnaneshwar, D., Ferreira, T. C., & Ngonga Ngomo, A.-C. (2020). NABU: Multilingual graph-based neural RDF verbalizer. arXiv preprint arXiv:2009.07728.
21. Neelakantan, A., Xu, T., Puri, R., Radford, A., Han, J. M., Tworek, J., Yuan, Q., Tezak, N., Kim, J. W., Hallacy, C., et al. (2022). Text and code embeddings by contrastive pretraining. arXiv preprint arXiv:2201.10005.
22. Reiter, E. (2018). A structured review of the validity of BLEU. Computational Linguistics, 44(3). https://doi.org/10.1162/colia00322.
23. Ribeiro, L. F. R., Zhang, Y., Gardent, C., & Gurevych, I. (2020). Modeling global and local node contexts for text generation from knowledge graphs. Transactions of the Association for Computational Linguistics, 8, 589–604.
24. Schamoni, S., Hieber, F., Sokolov, A., & Riezler, S. (2014). Learning translational and knowledge-based similarities from relevance rankings for cross-language retrieval. In Proceedings of the 52nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers) (pp. 488–494). Baltimore, Maryland: Association for Computational Linguistics.
25. Schmitt, M., Sharifzadeh, S., Tresp, V., & Schütze, H. (2020). An unsupervised joint system for text generation from knowledge graphs and semantic parsing. In Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP) (pp. 7117–7130). Association for Computational Linguistics.
26. Sha, L., Mou, L., Liu, T., Poupart, P., Li, S., Chang, B., & Sui, Z. (2018). Order-planning neural text generation from structured data. In Proceedings of the AAAI Conference on Artificial Intelligence (Vol. 32).
27. Vrandečić, D., & Krötzsch, M. (2014). Wikidata: A free collaborative knowledge base. Communications of the ACM, 57(10), 78–85.
