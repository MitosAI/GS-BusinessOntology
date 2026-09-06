# Benchmark-First Delivery Pattern — Business Reality Semantic Foundation

**Version:** v0.1  
**Status:** Active KOE research finding  
**Owner:** KOE-001  
**Architecture impact:** none — reinforces ADR-002

## Question

How should KOE move from the broad Business Reality Semantic Foundation into executable implementation without either overbuilding the first runtime or allowing a narrow pilot to redefine enterprise semantics?

## Evidence / public practice

### Evolutionary architecture / fitness functions

Thoughtworks' evolutionary-architecture practice defines architecture as supporting guided, incremental change and uses fitness functions to protect important architectural characteristics as the system evolves.

Source:
- Thoughtworks, *Building Evolutionary Architectures, 2nd Edition*: https://www.thoughtworks.com/insights/books/building-evolutionaryarchitectures-second-edition

### Small, self-contained changes

Google SRE release engineering recommends small, self-contained changes, automated tests, reproducible builds, and staged evaluation so failures are easier to detect and reverse.

Sources:
- Google SRE Workbook, *Canarying Releases*: https://sre.google/workbook/canarying-releases/
- Google, *Building Secure and Reliable Systems*, Chapter 7: https://google.github.io/building-secure-and-reliable-systems/raw/ch07.html

### Gradual qualification against real behavior

Google SRE's launch and canary guidance emphasizes gradual exposure and explicit verification rather than large all-at-once releases.

Source:
- Google SRE, *Reliable Product Launches*: https://sre.google/sre-book/reliable-product-launches/

## Synthesis

The consistent engineering pattern is:

1. keep the long-lived architecture broader than any one release;
2. implement small coherent vertical/incremental slices;
3. make architectural qualities executable as tests/fitness functions;
4. evaluate each increment against realistic behavior and data;
5. preserve reversibility and avoid coupling unrelated changes;
6. expand only after the previous slice demonstrates architectural fitness.

## GenSigma-specific implications

This directly supports the accepted ADR-002 split:

- **Business Reality Semantic Foundation** = broad enterprise compatibility envelope;
- **BUILD SPEC 001** = narrow first executable vertical slice selected from that envelope;
- each build must preserve the shared kernel invariants even when it implements only a subset of business objects;
- T01–T31 and FF-001–FF-010 should act as architectural fitness functions as implementation expands;
- later slices may add domains without redefining canonical identity, time, evidence, security, correction, or contextual-role semantics.

The first runtime should therefore be judged by whether it proves the hard invariants end-to-end, not by how many of the ~38 candidate objects it implements.

## Recommendation

Continue with a **walking-skeleton / evolutionary-slice** delivery posture:

```text
BROAD SEMANTIC FOUNDATION
        |
        v
SMALL EXECUTABLE SLICE
        |
        v
AUTOMATED SEMANTIC + ARCHITECTURE FITNESS TESTS
        |
        v
REALISTIC FIXTURE / EVIDENCE PRESSURE TEST
        |
        v
LEARN / CORRECT
        |
        v
NEXT SLICE
```

Keep each Codex task bounded and independently testable. Do not batch unrelated ontology, platform, connector, and cognition changes into one implementation increment.

## Remaining uncertainty / experiments

No new architecture decision is required. Empirical questions remain for Platform Engineering and later builds:

- latency/throughput at realistic evidence/object/link scale;
- persistence architecture fit;
- replay and recovery behavior;
- security filtering cost;
- operational complexity for the expected small team.

These should be resolved through benchmarks, not pre-emptive technology selection.

## Architecture disposition

**LOCAL_SOLVE / no new architecture question.** This research reinforces accepted ADR-002 and existing architecture-fitness doctrine.