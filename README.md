# AI Engineer Roadmap

> A comprehensive learning path from foundational ML to production AI agents.
> Focused on Data Scientist → AI Engineer career progression.

<p align="center">
  <img src="resources/roadmap-banner.png" alt="AI Engineer Roadmap" width="800">
</p>

## Overview

This repository provides a structured curriculum for becoming a proficient AI Engineer, with emphasis on:

- **Foundational understanding** of deep learning and transformers
- **Key research papers** that shaped modern AI (Attention Is All You Need → today)
- **Practical skills** for building and deploying AI agents
- **Career progression** from Data Scientist to AI Engineer

---

## 📚 Table of Contents

1. [Learning Path](#-learning-path)
2. [Part 1: Foundations](#part-1-foundations)
3. [Part 2: Transformers Deep Dive](#part-2-transformers-deep-dive)
4. [Part 3: Large Language Models](#part-3-large-language-models)
5. [Part 4: AI Agents](#part-4-ai-agents)
6. [Part 5: Production & Deployment](#part-5-production--deployment)
7. [Key Papers](#-key-papers-chronological)
8. [Projects](#-projects)
9. [Resources](#-resources)

---

## 🗺️ Learning Path

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        AI ENGINEER ROADMAP                               │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  PART 1: FOUNDATIONS (2-4 weeks)                                        │
│  ├── Linear Algebra & Calculus refresher                                │
│  ├── Neural Networks basics                                             │
│  ├── PyTorch fundamentals                                               │
│  └── CNNs and RNNs overview                                             │
│                          ↓                                               │
│  PART 2: TRANSFORMERS (3-4 weeks)                                       │
│  ├── Attention mechanism                                                │
│  ├── "Attention Is All You Need" paper                                  │
│  ├── Encoder-Decoder architecture                                       │
│  ├── Positional encoding                                                │
│  └── Implement transformer from scratch                                 │
│                          ↓                                               │
│  PART 3: LARGE LANGUAGE MODELS (4-6 weeks)                             │
│  ├── GPT architecture (decoder-only)                                    │
│  ├── BERT and encoder models                                            │
│  ├── Scaling laws                                                       │
│  ├── Training and fine-tuning                                           │
│  ├── RLHF and alignment                                                 │
│  └── Prompting and in-context learning                                  │
│                          ↓                                               │
│  PART 4: AI AGENTS (4-6 weeks)                                         │
│  ├── Agent architectures (ReAct, CoT, ToT)                             │
│  ├── Tool use and function calling                                      │
│  ├── Memory systems                                                     │
│  ├── Multi-agent systems                                                │
│  ├── Agent frameworks (LangChain, LangGraph, Claude)                   │
│  └── MCP (Model Context Protocol)                                       │
│                          ↓                                               │
│  PART 5: PRODUCTION (2-4 weeks)                                        │
│  ├── Deployment strategies                                              │
│  ├── Evaluation and monitoring                                          │
│  ├── Cost optimization                                                  │
│  └── Safety and guardrails                                              │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Part 1: Foundations

**Goal:** Build strong fundamentals in neural networks and PyTorch.

### 1.1 Math Refresher
| Topic | Resource | Type |
|-------|----------|------|
| Linear Algebra | [3Blue1Brown - Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) | Video |
| Calculus | [3Blue1Brown - Essence of Calculus](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr) | Video |
| Probability | [StatQuest - Statistics Fundamentals](https://www.youtube.com/playlist?list=PLblh5JKOoLUK0FLuzwntyYI10UQFUhsY9) | Video |

### 1.2 Neural Networks
| Topic | Resource | Type |
|-------|----------|------|
| NN from scratch | [Andrej Karpathy - Neural Networks: Zero to Hero](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ) | Video |
| Deep Learning book | [Deep Learning - Goodfellow et al.](https://www.deeplearningbook.org/) | Book |
| Fast.ai course | [Practical Deep Learning for Coders](https://course.fast.ai/) | Course |

### 1.3 PyTorch
| Topic | Resource | Type |
|-------|----------|------|
| PyTorch basics | [PyTorch Official Tutorials](https://pytorch.org/tutorials/) | Tutorial |
| PyTorch Lightning | [Lightning AI Tutorials](https://lightning.ai/docs/pytorch/stable/tutorials.html) | Tutorial |

### 📓 Notebooks
- [ ] `notebooks/01_pytorch_basics.ipynb` - PyTorch tensors and autograd
- [ ] `notebooks/02_simple_nn.ipynb` - Build a simple neural network
- [ ] `notebooks/03_cnn_mnist.ipynb` - CNN for image classification

---

## Part 2: Transformers Deep Dive

**Goal:** Deeply understand the Transformer architecture.

### 2.1 Attention Mechanism
| Topic | Resource | Type |
|-------|----------|------|
| Visual intro | [3Blue1Brown - Attention in transformers](https://www.youtube.com/watch?v=eMlx5fFNoYc) | Video |
| Illustrated Guide | [Jay Alammar - The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) | Article |
| LLM Visualization | [Brendan Bycroft - LLM Visualization](https://bbycroft.net/llm) | Interactive |

### 2.2 Core Papers
| Paper | Year | Key Contribution |
|-------|------|------------------|
| [Attention Is All You Need](https://arxiv.org/abs/1706.03762) | 2017 | Introduced the Transformer |
| [BERT](https://arxiv.org/abs/1810.04805) | 2018 | Bidirectional pre-training |
| [GPT-2](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) | 2019 | Scaled decoder-only models |

### 2.3 Implementation
| Topic | Resource | Type |
|-------|----------|------|
| Annotated Transformer | [Harvard NLP - The Annotated Transformer](http://nlp.seas.harvard.edu/annotated-transformer/) | Code |
| nanoGPT | [Karpathy - nanoGPT](https://github.com/karpathy/nanoGPT) | Code |
| minGPT | [Karpathy - minGPT](https://github.com/karpathy/minGPT) | Code |

### 📓 Notebooks
- [ ] `notebooks/04_attention_from_scratch.ipynb` - Implement self-attention
- [ ] `notebooks/05_transformer_encoder.ipynb` - Build transformer encoder
- [ ] `notebooks/06_gpt_from_scratch.ipynb` - Build GPT from scratch

---

## Part 3: Large Language Models

**Goal:** Understand how modern LLMs work and how to use them effectively.

### 3.1 Architecture Evolution
| Model | Paper | Key Innovation |
|-------|-------|----------------|
| GPT-3 | [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) | In-context learning, scaling |
| InstructGPT | [Training language models to follow instructions](https://arxiv.org/abs/2203.02155) | RLHF |
| GPT-4 | [GPT-4 Technical Report](https://arxiv.org/abs/2303.08774) | Multimodal, improved reasoning |
| Llama 2 | [Llama 2: Open Foundation](https://arxiv.org/abs/2307.09288) | Open weights |
| Claude | [Constitutional AI](https://arxiv.org/abs/2212.08073) | AI safety approach |
| Mistral | [Mistral 7B](https://arxiv.org/abs/2310.06825) | Efficient architecture |

### 3.2 Training & Fine-tuning
| Topic | Resource | Type |
|-------|----------|------|
| Pre-training | [Chinchilla - Training Compute-Optimal LLMs](https://arxiv.org/abs/2203.15556) | Paper |
| Fine-tuning | [LoRA: Low-Rank Adaptation](https://arxiv.org/abs/2106.09685) | Paper |
| RLHF | [Anthropic RLHF Guide](https://arxiv.org/abs/2204.05862) | Paper |
| DPO | [Direct Preference Optimization](https://arxiv.org/abs/2305.18290) | Paper |

### 3.3 Prompting
| Topic | Resource | Type |
|-------|----------|------|
| Prompt Engineering | [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering) | Guide |
| Chain-of-Thought | [Chain-of-Thought Prompting](https://arxiv.org/abs/2201.11903) | Paper |
| Few-shot learning | [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) | Paper |

### 📓 Notebooks
- [ ] `notebooks/07_llm_inference.ipynb` - Run local LLMs with Ollama
- [ ] `notebooks/08_finetuning_lora.ipynb` - Fine-tune with LoRA
- [ ] `notebooks/09_prompting_techniques.ipynb` - Advanced prompting

---

## Part 4: AI Agents

**Goal:** Build autonomous AI systems that can reason and take actions.

### 4.1 Agent Architectures
| Pattern | Paper/Resource | Description |
|---------|----------------|-------------|
| ReAct | [ReAct: Synergizing Reasoning and Acting](https://arxiv.org/abs/2210.03629) | Reasoning + Action loops |
| Chain-of-Thought | [Chain-of-Thought Prompting](https://arxiv.org/abs/2201.11903) | Step-by-step reasoning |
| Tree of Thoughts | [Tree of Thoughts](https://arxiv.org/abs/2305.10601) | Branching reasoning |
| Reflexion | [Reflexion](https://arxiv.org/abs/2303.11366) | Self-reflection and learning |

### 4.2 Tool Use & Function Calling
| Topic | Resource | Type |
|-------|----------|------|
| Function calling | [OpenAI Function Calling](https://platform.openai.com/docs/guides/function-calling) | Guide |
| Tool use | [Anthropic Tool Use](https://docs.anthropic.com/en/docs/tool-use) | Guide |
| MCP | [Model Context Protocol](https://modelcontextprotocol.io/) | Specification |

### 4.3 Memory Systems
| Type | Description | Use Case |
|------|-------------|----------|
| Short-term | Conversation context | Chat history |
| Long-term | Vector databases | Knowledge retrieval |
| Episodic | Experience storage | Learning from past |
| Semantic | Knowledge graphs | Structured knowledge |

### 4.4 Agent Frameworks
| Framework | Focus | Best For |
|-----------|-------|----------|
| [LangChain](https://langchain.com/) | General purpose | Rapid prototyping |
| [LangGraph](https://langchain-ai.github.io/langgraph/) | Stateful agents | Complex workflows |
| [Claude Code](https://docs.anthropic.com/en/docs/claude-code) | Terminal AI | Development tasks |
| [CrewAI](https://www.crewai.com/) | Multi-agent | Team simulations |
| [AutoGen](https://microsoft.github.io/autogen/) | Conversational | Agent conversations |

### 4.5 Multi-Agent Systems
| Paper | Key Contribution |
|-------|------------------|
| [Generative Agents](https://arxiv.org/abs/2304.03442) | Believable agent simulations |
| [CAMEL](https://arxiv.org/abs/2303.17760) | Role-playing agent communication |
| [AutoGen](https://arxiv.org/abs/2308.08155) | Multi-agent conversations |

### 📓 Notebooks
- [ ] `notebooks/10_basic_agent.ipynb` - Build a simple ReAct agent
- [ ] `notebooks/11_tool_use.ipynb` - Implement tool calling
- [ ] `notebooks/12_rag_agent.ipynb` - RAG-powered agent
- [ ] `notebooks/13_multi_agent.ipynb` - Multi-agent system

---

## Part 5: Production & Deployment

**Goal:** Deploy and maintain AI systems in production.

### 5.1 Deployment
| Topic | Resource | Type |
|-------|----------|------|
| API Design | REST/gRPC patterns | Guide |
| Containerization | Docker + Kubernetes | Tutorial |
| Serverless | Modal, AWS Lambda | Platform |

### 5.2 Evaluation
| Topic | Resource | Type |
|-------|----------|------|
| LLM Evaluation | [HELM](https://crfm.stanford.edu/helm/) | Benchmark |
| Agent Evaluation | [AgentBench](https://github.com/THUDM/AgentBench) | Benchmark |
| Human Evaluation | Annotation guidelines | Practice |

### 5.3 Cost Optimization
| Strategy | Description |
|----------|-------------|
| Caching | Store frequent responses |
| Batching | Group requests |
| Model selection | Right-size for task |
| Prompt optimization | Reduce tokens |

### 5.4 Safety & Guardrails
| Topic | Resource |
|-------|----------|
| Content filtering | OpenAI Moderation API |
| Output validation | Guardrails AI |
| Jailbreak prevention | Prompt injection defense |

---

## 📄 Key Papers (Chronological)

### 2017 - The Transformer Era Begins
| Paper | Citation | Impact |
|-------|----------|--------|
| [Attention Is All You Need](https://arxiv.org/abs/1706.03762) | Vaswani et al. | Introduced Transformers |

### 2018 - Pre-training Revolution
| Paper | Citation | Impact |
|-------|----------|--------|
| [BERT](https://arxiv.org/abs/1810.04805) | Devlin et al. | Bidirectional pre-training |
| [GPT](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf) | Radford et al. | Generative pre-training |

### 2019 - Scaling Up
| Paper | Citation | Impact |
|-------|----------|--------|
| [GPT-2](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) | Radford et al. | Showed scaling potential |
| [RoBERTa](https://arxiv.org/abs/1907.11692) | Liu et al. | Optimized BERT training |

### 2020 - The GPT-3 Moment
| Paper | Citation | Impact |
|-------|----------|--------|
| [GPT-3](https://arxiv.org/abs/2005.14165) | Brown et al. | Few-shot learning |
| [Scaling Laws](https://arxiv.org/abs/2001.08361) | Kaplan et al. | Predictable scaling |

### 2021 - Efficiency & Instruction
| Paper | Citation | Impact |
|-------|----------|--------|
| [LoRA](https://arxiv.org/abs/2106.09685) | Hu et al. | Efficient fine-tuning |
| [FLAN](https://arxiv.org/abs/2109.01652) | Wei et al. | Instruction tuning |

### 2022 - ChatGPT Era
| Paper | Citation | Impact |
|-------|----------|--------|
| [InstructGPT](https://arxiv.org/abs/2203.02155) | Ouyang et al. | RLHF |
| [Chain-of-Thought](https://arxiv.org/abs/2201.11903) | Wei et al. | Reasoning prompting |
| [Chinchilla](https://arxiv.org/abs/2203.15556) | Hoffmann et al. | Compute-optimal training |
| [Constitutional AI](https://arxiv.org/abs/2212.08073) | Bai et al. | AI safety approach |

### 2023 - Agents & Multimodal
| Paper | Citation | Impact |
|-------|----------|--------|
| [GPT-4](https://arxiv.org/abs/2303.08774) | OpenAI | Multimodal, improved reasoning |
| [LLaMA](https://arxiv.org/abs/2302.13971) | Touvron et al. | Open model release |
| [ReAct](https://arxiv.org/abs/2210.03629) | Yao et al. | Agent reasoning |
| [Generative Agents](https://arxiv.org/abs/2304.03442) | Park et al. | Believable agents |
| [Tree of Thoughts](https://arxiv.org/abs/2305.10601) | Yao et al. | Complex reasoning |
| [DPO](https://arxiv.org/abs/2305.18290) | Rafailov et al. | Simpler alignment |
| [Llama 2](https://arxiv.org/abs/2307.09288) | Touvron et al. | Open + commercial |

### 2024 - Agents Scale Up
| Paper | Citation | Impact |
|-------|----------|--------|
| [Mixtral](https://arxiv.org/abs/2401.04088) | Mistral AI | MoE efficiency |
| [Claude 3](https://www.anthropic.com/claude) | Anthropic | Improved capabilities |
| [Llama 3](https://ai.meta.com/blog/meta-llama-3/) | Meta | Open frontier model |

### 2025-2026 - Current Frontier
| Development | Impact |
|-------------|--------|
| Claude Opus 4.5 | Current state-of-the-art |
| MCP Protocol | Standardized tool use |
| Multi-agent production | Real-world agent deployments |

---

## 🛠️ Projects

### Beginner
1. **Sentiment Analyzer** - Fine-tune a model for sentiment analysis
2. **Q&A Bot** - Build a simple question-answering system
3. **Text Summarizer** - Implement extractive and abstractive summarization

### Intermediate
4. **RAG System** - Build retrieval-augmented generation
5. **Code Assistant** - Create a coding helper with tool use
6. **Research Agent** - Agent that searches and synthesizes information

### Advanced
7. **Multi-Agent System** - Coordinate multiple specialized agents
8. **Custom Fine-tuned Model** - Train a domain-specific model
9. **Production Agent** - Deploy a full agent system with monitoring

---

## 📚 Resources

### Books
- [Deep Learning](https://www.deeplearningbook.org/) - Goodfellow, Bengio, Courville
- [Dive into Deep Learning](https://d2l.ai/) - Interactive deep learning book
- [Natural Language Processing with Transformers](https://www.oreilly.com/library/view/natural-language-processing/9781098136789/) - Tunstall et al.

### Courses
- [Stanford CS224N - NLP with Deep Learning](https://web.stanford.edu/class/cs224n/)
- [Stanford CS25 - Transformers United](https://web.stanford.edu/class/cs25/)
- [Fast.ai - Practical Deep Learning](https://course.fast.ai/)
- [DeepLearning.AI - LLM Courses](https://www.deeplearning.ai/)

### YouTube Channels
- [Andrej Karpathy](https://www.youtube.com/@AndrejKarpathy) - Neural networks deep dives
- [3Blue1Brown](https://www.youtube.com/@3blue1brown) - Visual math explanations
- [Yannic Kilcher](https://www.youtube.com/@YannicKilcher) - Paper explanations
- [AI Explained](https://www.youtube.com/@aiexplained-official) - AI news and analysis

### Communities
- [r/MachineLearning](https://www.reddit.com/r/MachineLearning/)
- [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/)
- [Hugging Face Forums](https://discuss.huggingface.co/)
- [LangChain Discord](https://discord.gg/langchain)

### Reference Repositories
- [mlabonne/llm-course](https://github.com/mlabonne/llm-course) - Comprehensive LLM course
- [labmlai/annotated_deep_learning_paper_implementations](https://github.com/labmlai/annotated_deep_learning_paper_implementations) - Paper implementations
- [floodsung/Deep-Learning-Papers-Reading-Roadmap](https://github.com/floodsung/Deep-Learning-Papers-Reading-Roadmap) - Paper reading guide
- [dair-ai/Transformers-Recipe](https://github.com/dair-ai/Transformers-Recipe) - Transformer study guide

---

## Progress Tracker

```
[ ] Part 1: Foundations
    [ ] Math refresher
    [ ] Neural networks
    [ ] PyTorch basics

[ ] Part 2: Transformers
    [ ] Attention mechanism
    [ ] Read "Attention Is All You Need"
    [ ] Implement transformer from scratch

[ ] Part 3: LLMs
    [ ] Understand GPT architecture
    [ ] Learn fine-tuning (LoRA)
    [ ] Practice prompting techniques

[ ] Part 4: AI Agents
    [ ] Build ReAct agent
    [ ] Implement tool use
    [ ] Create multi-agent system

[ ] Part 5: Production
    [ ] Deploy an agent
    [ ] Set up monitoring
    [ ] Optimize costs
```

---

## Contributing

This is a personal learning repository, but suggestions are welcome. Open an issue or PR if you have resources to add.

---

## License

MIT License - Feel free to use and adapt for your own learning journey.

---

*Last updated: January 2026*

*Inspired by [mlabonne/llm-course](https://github.com/mlabonne/llm-course), [labmlai/annotated_deep_learning_paper_implementations](https://github.com/labmlai/annotated_deep_learning_paper_implementations), and [dair-ai/Transformers-Recipe](https://github.com/dair-ai/Transformers-Recipe)*
