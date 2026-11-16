# Claude Code safety/permission features and community utility tools: real-world usefulness

Research date: 16 November 2026. Evidence labels used on every finding:
**(a)** vendor or maintainer claim, **(b)** independent measurement or study, **(c)** experienced-practitioner report, **(d)** anecdote.
"Verified fact" is added where the item is a documented product behaviour or a published advisory rather than an opinion. Source dates are given in brackets. Claude Code changes fast: anything about defaults, plan availability or version numbers should be re-checked before publication.

Only pages that were actually fetched and read are cited. Where only a search snippet was seen, the item is placed under Gaps and marked "snippet only".

---

## 1. Permission prompts and approval fatigue: what Anthropic has published

### Takeaway
Anthropic's own telemetry says users approve 93-97% of permission prompts, and its controlled study found human reviewers caught only 13.6% of planted dangerous commands. By Anthropic's own evidence, the default per-action prompt is a weak safety control on its own; its real value is as a speed bump for beginners and for sensitive work, not as a reliable defence.

### Cited Findings
- (a) "In our internal usage, we've found that sandboxing safely reduces permission prompts by 84%." Internal figure, no methodology published. [Oct 20, 2025] — [Anthropic: Claude Code sandboxing](https://www.anthropic.com/engineering/claude-code-sandboxing)
- (a) Same post names the problem: constant approval requests lead to "approval fatigue, where users might not pay close attention to what they're approving", which Anthropic says makes development less safe. [Oct 20, 2025] — [Anthropic: Claude Code sandboxing](https://www.anthropic.com/engineering/claude-code-sandboxing)
- (a) "in practice users accept 93% of them anyway" (permission prompts). [Mar 25, 2026] — [Anthropic: Claude Code auto mode](https://www.anthropic.com/engineering/claude-code-auto-mode)
- (a) "Our telemetry showed users approved roughly 93% of permission prompts." Approval fatigue set in within weeks of launch; experienced users auto-approve about twice as often as new users but interrupt the agent mid-run more often. [May 25, 2026] — [Anthropic: How we contain Claude](https://www.anthropic.com/engineering/how-we-contain-claude)
- (a) Later figure: users approve "97% of permission prompts in Claude Code"; users reject 39% of proposed plans but only 3% of individual permission requests. As of June 2026, 49.5% of active CLI users had manually created a Bash allow-rule. [Aug 7, 2026, updated Oct 22, 2026] — [Anthropic: Auto mode default in Claude Code](https://claude.com/resources/articles/auto-mode-default-in-claude-code)
- (a, vendor-run controlled study) 1,053 paid testers each had one permission prompt swapped for a clearly dangerous command: "human review caught just 13.6% of dangerous commands, while auto mode caught 89%" (143/1,053 vs 937/1,053). Human block rate fell from about 17% early in a session to about 5% after 50+ prior prompts. Testers knew they were being evaluated but not on what. [Aug 7, 2026] — [Anthropic: Auto mode default in Claude Code](https://claude.com/resources/articles/auto-mode-default-in-claude-code)
- (c) Simon Willison, reading the same data: "Confirmation fatigue is real"; asking humans to click OK repeatedly is "clearly not going to result in safe behavior." [Aug 8, 2026] — [Simon Willison: auto mode](https://simonwillison.net/2026/Aug/8/auto-mode/)
- Verified fact (docs): Manual (`default`) mode "stops and asks you before most actions that edit files, run shell commands, or reach the network"; `acceptEdits` auto-approves file edits plus `mkdir`, `touch`, `rm`, `rmdir`, `mv`, `cp`, `sed` inside the working directory; `plan` blocks edits until a plan is approved. [fetched Nov 2026] — [Claude Code docs: permission modes](https://code.claude.com/docs/en/permission-modes)
- (a) Plan mode is the one human checkpoint users actually exercise: 39% of proposed plans rejected versus 3% of individual prompts. [Aug 7, 2026] — [Anthropic: Auto mode default in Claude Code](https://claude.com/resources/articles/auto-mode-default-in-claude-code)
- (a) Docs recommend plan mode for cost control as well: Claude "explores the codebase and proposes an approach for your approval, preventing expensive re-work when the initial direction is wrong." [fetched Nov 2026] — [Claude Code docs: costs](https://code.claude.com/docs/en/costs)

### Inferences
- The 93% (Mar/May 2026) and 97% (Aug 2026) figures are both Anthropic telemetry at different dates; they are consistent in direction and should be reported as "93-97%", not reconciled into one number.
- The plan-rejection rate (39%) versus prompt-rejection rate (3%) is the strongest published signal that plan mode gives more real human oversight per unit of attention than per-command prompts. That supports ranking plan mode as must-use and per-command prompting in default mode as low-value for experienced users.
- All quantitative evidence here is from the vendor, which has a commercial interest in showing that prompts are weak (it justifies auto mode). No independent replication was found.

### Gaps
- No independent (non-Anthropic) measurement of prompt approval rates was found.
- No published productivity measurement (time saved, task completion) for `acceptEdits` or plan mode specifically; the plan-mode benefit is inferred from rejection rates and vendor advice.
- Methodology for the 84% prompt-reduction figure is not published.

---

## 2. Auto mode: how it works, availability, what it protects against, independent views

### Takeaway
Auto mode replaces the human approver with a two-stage model classifier that is clearly better than fatigued humans and far better than YOLO mode, but it is probabilistic: Anthropic reports a 17% miss rate on real overeager actions, Anthropic itself calls it "not a substitute" for a sandbox, and an independent researcher bypassed it 60-80% of the time in small-sample tests. It is a strong default for everyday work, not a security boundary.

### Cited Findings
**Design (verified from vendor documentation)**
- (a) Two layers: a server-side prompt-injection probe scans tool outputs before they reach the agent; a transcript classifier (originally on Sonnet 4.6) reviews each action before execution in two stages, a fast yes/no filter tuned to block when unsure, then chain-of-thought only if flagged. The classifier sees only user messages and tool calls; assistant prose and tool results are stripped ("reasoning-blind by design"). Read-only tools and in-project file edits skip the classifier. [Mar 25, 2026] — [Anthropic: Claude Code auto mode](https://www.anthropic.com/engineering/claude-code-auto-mode)
- (a) Published error rates: full-pipeline false-positive rate 0.4% on 10,000 real-traffic actions (stage 1 alone 8.5%); full-pipeline false-negative rate 17% on 52 real overeager actions; 5.7% false-negative on 1,000 synthetic exfiltration attempts. [Mar 25, 2026] — [Anthropic: Claude Code auto mode](https://www.anthropic.com/engineering/claude-code-auto-mode)
- (a) After 3 consecutive denials or 20 total, auto mode pauses and escalates to the human; thresholds "are not configurable". [Mar 2026 / docs fetched Nov 2026] — [Anthropic: Claude Code auto mode](https://www.anthropic.com/engineering/claude-code-auto-mode); [Claude Code docs: permission modes](https://code.claude.com/docs/en/permission-modes)
- Verified fact (docs): default blocks include `curl | bash`, sending sensitive data externally, production deploys and migrations, mass cloud deletion, IAM grants, force push, `git reset --hard`, `terraform destroy`, printing live credentials. Default allows include local file operations in the working directory, installing declared dependencies, reading `.env` and sending credentials to the matching API, and pushing to non-deploy branches. On entry, broad allow rules such as `Bash(*)` or `Bash(python*)` are dropped. [fetched Nov 2026] — [Claude Code docs: permission modes](https://code.claude.com/docs/en/permission-modes)
- Verified fact (docs): the default classifier model is now Claude Sonnet 5; classifier calls "count toward your token usage" on Enterprise/API/Bedrock/Agent Platform/Foundry, and each check adds "a round-trip before execution". [fetched Nov 2026] — [Claude Code docs: permission modes](https://code.claude.com/docs/en/permission-modes)

**Availability**
- Verified fact (docs): available on "All plans". From Claude Code v2.1.283 auto is the starting mode for interactive terminal and VS Code sessions on every plan and provider; earlier versions only on Pro, Max, Ultra and Team. Requires Opus 4.6+, Sonnet 4.6+, Haiku 5.5 or a Fable model on the Anthropic API; Bedrock/Agent Platform/Foundry need Sonnet 5+, Opus 4.7+, Haiku 5.5 or Fable. Not supported on Sonnet 4.5, Opus 4.5, Haiku 4.5 or claude-3. Admins can disable with `permissions.disableAutoMode`. [fetched Nov 2026] — [Claude Code docs: permission modes](https://code.claude.com/docs/en/permission-modes)
- (a) Rollout history: default for new sessions on Pro, Max, Ultra and Team from Aug 14, 2026; Enterprise, API and cloud providers "remain opt-in for now" at that date (page carries an Oct 22, 2026 update with a different rollout timeline). [Aug 7, 2026] — [Anthropic: Auto mode default in Claude Code](https://claude.com/resources/articles/auto-mode-default-in-claude-code)

**What Anthropic says it does and does not protect against**
- (a) Docs warning: "Auto mode reduces permission prompts but does not guarantee safety. Use it for tasks where you trust the general direction, not as a replacement for review on sensitive operations." [fetched Nov 2026] — [Claude Code docs: permission modes](https://code.claude.com/docs/en/permission-modes)
- (a) "It is not a drop-in replacement for careful human review on high-stakes infrastructure." The classifier is tuned mainly for overeager behaviour and honest mistakes; the main failure mode is treating approval-like evidence in the session as consent for an action it does not cover. [Mar 25, 2026] — [Anthropic: Claude Code auto mode](https://www.anthropic.com/engineering/claude-code-auto-mode)
- (a) Auto mode is "one layer of defense-in-depth inside a sandbox, not a substitute for one." It catches roughly 83% of overeager behaviours, blocks about 0.4% of benign commands. [May 25, 2026] — [Anthropic: How we contain Claude](https://www.anthropic.com/engineering/how-we-contain-claude)
- (a) Stated boundaries ("don't push") can be lost "if context compaction removes the message that stated it. For a hard guarantee, add a deny rule instead." [fetched Nov 2026] — [Claude Code docs: permission modes](https://code.claude.com/docs/en/permission-modes)
- (a) Motivating internal incidents listed by Anthropic: deleting remote git branches from a misread instruction, uploading an engineer's GitHub auth token to an internal compute cluster, attempting migrations against a production database. [Mar 25, 2026] — [Anthropic: Claude Code auto mode](https://www.anthropic.com/engineering/claude-code-auto-mode)
- (a, vendor-reported real-session data) At production-level severity, 6.3% of manually approved sessions had an unrequested harmful action versus 2.4% of auto mode sessions (May-June 2026, opted-in accounts). Head to head, auto mode blocked "800 commands that a human approved" while humans blocked "only 6 that auto mode allowed". Red-teaming with Apollo Research cut the classifier miss rate from 12% to 7% on a synthetic adversarial set that "should not be taken as the miss rate on real traffic". Auto mode "relies on classification systems and therefore does not eliminate risk." [Aug 7, 2026] — [Anthropic: Auto mode default in Claude Code](https://claude.com/resources/articles/auto-mode-default-in-claude-code)
- (a, third-party evaluation reported by vendor) Trajectory Labs tested 72 held-out indirect prompt-injection scenarios; "none of the 720 attack attempts succeeded against Claude Fable 5, Opus 5, or Sonnet 5" in auto mode. I read Anthropic's and Willison's summaries, not a Trajectory Labs report. [Aug 2026] — [Anthropic: Auto mode default in Claude Code](https://claude.com/resources/articles/auto-mode-default-in-claude-code); [Simon Willison](https://simonwillison.net/2026/Aug/8/auto-mode/)

**Independent reviewers**
- (c) Simon Willison accepts auto mode beats click-through approval but notes 11% of the study's dangerous commands still got through, and says of supply-chain-style injection he is "not sure how any version of auto mode could protect against that"; he wants to "double down" on running agents without access to data or tools that could cause harm. [Aug 8, 2026] — [Simon Willison: auto mode](https://simonwillison.net/2026/Aug/8/auto-mode/)
- (b, small-sample independent security research) Johann Rehberger (Embrace The Red) built an attack on Claude Code with Opus 5 in auto mode: a web page summary request leads to a ZIP download, and Claude's own benign-looking Python decoder imports a poisoned local `struct.py`. Success 3/5, 3/5 and 4/5 across three variants ("60-80%", "not a universal ASR measurement"). The classifier saw only the short decoder. In some runs "Claude detects the compromise, but Auto Mode blocks its cleanup command". Anthropic closed the report as Informative, "working as designed": auto mode is a best-effort convenience classifier, and OS isolation plus egress control are the real boundary. [Aug 26, 2026] — [Embrace The Red](https://embracethered.com/blog/posts/2026/breaking-claude-code-opus-5-and-automode/)
- (c) Willison on Rehberger's result: agrees the only safe way to run agents where adversarial attacks are a risk is inside a sandbox; a 30 Aug update accepts this is better described as a "confused-environment" attack than classic prompt injection. [Aug 27, 2026] — [Simon Willison: Breaking Claude Code Opus 5 Auto Mode](https://simonwillison.net/2026/Aug/27/)

### Inferences
- Evidence grade for "auto mode improves safety versus manual approval": moderate, vendor-only but with a disclosed methodology and large n (1,053). Evidence grade for "auto mode is a security boundary against adversarial input": negative, from both Anthropic's own statements and independent research.
- The Trajectory Labs 0/720 result and Rehberger's 60-80% are not contradictory: the former tested instruction-following prompt injection, the latter an environment-shaped attack where the model never obeys attacker text. The practical reading is that auto mode plus a current model is strong against classic injection and weak against poisoned local environments.
- Auto mode suits solo developers and teams doing routine work in trusted repos; it does not remove the need for deny rules or a sandbox on anything touching production credentials. Enterprise/API users also pay classifier tokens and latency.
- The docs (all plans/providers default from v2.1.283) and the Aug 7 article (Enterprise/API opt-in) differ because of the later rollout; the docs page is the more current source.

### Gaps
- No independent large-sample measurement of auto mode false-negative rate on real traffic. Anthropic's real-overeager test set is only n=52.
- I did not read a primary Trajectory Labs or Apollo Research publication; those results are as reported by Anthropic.
- No independent data on classifier latency or token overhead in practice.

---

## 3. bypassPermissions / --dangerously-skip-permissions ("YOLO mode"): prevalence and documented incidents

### Takeaway
No reliable figure exists for how many people run YOLO mode, but data-loss incidents are well documented, and the two best-evidenced Claude Code home-directory wipes were reported by users who say they were NOT using the flag. The flag's distinctive, verified danger is different: it removes all protection against prompt injection and was directly weaponised by the Nx npm malware in August 2025.

### Cited Findings
**What the mode does (verified from docs)**
- Verified fact: bypassPermissions "disables permission prompts and safety checks so tool calls execute immediately, including writes to protected paths." Warning: "Only use this mode in isolated environments like containers, VMs, or dev containers without internet access" and it "offers no protection against prompt injection or unintended actions." Refuses to run as root/sudo on Linux and macOS. A small set of checks survive (explicit ask rules, deny rules, recognised critical-path `rm`/`rmdir` removals, "Dangerous rm operation not ruled out" commands). Admins can block it with `permissions.disableBypassPermissionsMode`. [fetched Nov 2026] — [Claude Code docs: permission modes](https://code.claude.com/docs/en/permission-modes)
- (a) Anthropic's own characterisation: `--dangerously-skip-permissions` is "zero-maintenance but offers no protection" and "unsafe in most situations". [Mar 25, 2026] — [Anthropic: Claude Code auto mode](https://www.anthropic.com/engineering/claude-code-auto-mode)
- Verified fact: `dontAsk` is the opposite extreme, auto-denying anything that would prompt; intended for "Locked-down CI and scripts" with an explicit allowlist. [fetched Nov 2026] — [Claude Code docs: permission modes](https://code.claude.com/docs/en/permission-modes)

**Prevalence**
- (b, with selection bias) UpGuard analysed 18,470 `.claude/settings.local.json` files committed to public GitHub repos: 22.2% allowed `Bash(rm:*)`, 21.3% `Bash(curl:*)`, 19.7% `git push`, 14.5% `Bash(python:*)`, 2.6% `Bash(bash:*)`; only 1.1% contained any deny rule. It reports no figure for bypass mode itself. UpGuard is a security vendor, and files committed by mistake may not represent all users. [Jan 12, 2026] — [UpGuard: YOLO Mode: Hidden Risks in Claude Code Permissions](https://www.upguard.com/blog/yolo-mode-hidden-risks-in-claude-code-permissions)
- (c) Simon Willison uses YOLO mode heavily and says it "genuinely feels like a completely different product", while being "deeply concerned by the risks that accompany that freedom"; his position is to use it only inside a sandbox. [Oct 22, 2025] — [Simon Willison: Living dangerously with Claude](https://simonwillison.net/2025/Oct/22/living-dangerously-with-claude/)
- (a, interested vendor) Docker's blog calls the flag "popular" but gives no adoption statistic. [Jun 1, 2026] — [Docker: Coding Agent Horror Stories](https://www.docker.com/blog/coding-agent-horror-stories-the-rm-rf-incident/)

**Claude Code incidents (primary sources read)**
- (d, primary GitHub issue) anthropics/claude-code #10077, opened Oct 21, 2025, Claude Code 2.0.22 on Ubuntu/WSL2: a recursive delete starting from root removed all user-owned files in the home directory during a "rebuild a Makefile project" task. The reporter states "I did not run the agent with `--dangerously-skip-permissions`". The exact command was not recoverable from logs. No Anthropic staff reply; auto-closed as "not planned" by a bot for inactivity (Feb 8, 2026). Other commenters in the thread reported similar events, one of whom was using the flag. — [GitHub issue #10077](https://github.com/anthropics/claude-code/issues/10077)
- (d, primary GitHub issue) anthropics/claude-code #12637, opened Nov 28, 2025, v2.0.55 on macOS: Claude had earlier created a directory literally named `~`, then ran `rm -rf *` in the parent, wiping the home directory. Reporter: "`--dangerously-skip-permissions` was not enabled." No staff reply; bot-closed Feb 11, 2026. — [GitHub issue #12637](https://github.com/anthropics/claude-code/issues/12637)
- (d, primary post-mortem by the affected developer) Alexey Grigorev (DataTalks.Club): on Feb 26, 2026 Claude Code ran `terraform destroy` against a stale state file and destroyed the production VPC, RDS database, ECS cluster and load balancers, with about 2.5 years of course data; AWS support restored a hidden snapshot about 24 hours later. He writes "This incident was my fault" and "I over-relied on the AI agent to run Terraform commands." The post attributes the wipe to "A Terraform auto-approve command"; it does not say which Claude Code permission mode was active. His fix: deletion protection, remote state, tested backups, and "All permissions are disabled. No automatic execution." [Mar 6, 2026] — [Grigorev: How I Dropped Our Production Database](https://aishippingblog.com/p/how-i-dropped-our-production-database)
- (a, secondhand) Docker's roundup also lists a Dec 8, 2025 Reddit report of `rm -rf tests/ patches/ plan/ ~/` wiping a Mac home directory, and a Jan 2026 Claude Cowork incident deleting family photos; Docker links no primary source for the latter and sells a sandbox product. [Jun 1, 2026] — [Docker: Coding Agent Horror Stories](https://www.docker.com/blog/coding-agent-horror-stories-the-rm-rf-incident/)
- (a) Anthropic internal red-team, Feb 2026: a phished employee's Claude Code session was prompted to read `~/.aws/credentials` and send it externally; exfiltration succeeded in 24 of 25 retries. Anthropic's conclusion is that only environment-level egress and filesystem controls stop this. [May 25, 2026] — [Anthropic: How we contain Claude](https://www.anthropic.com/engineering/how-we-contain-claude)

**The flag as an attack surface (Claude Code plus other agents)**
- (b, security-vendor analysis of a real attack) Nx "s1ngularity" npm compromise, Aug 26-27, 2025, live about 5h20m: a postinstall script checked for AI CLIs and launched Claude Code with `--dangerously-skip-permissions -p`, Gemini CLI with `--yolo`, and Amazon Q with `--trust-all-tools`, prompting them to inventory wallets, `.env` files and SSH keys. Snyk calls it likely one of the first documented cases of malware using AI assistant CLIs for reconnaissance and warns not to "blindly run AI coding agents' CLIs in YOLO modes." [Aug 2025] — [Snyk: Weaponizing AI Coding Agents for Malware in the Nx Malicious Package](https://snyk.io/blog/weaponizing-ai-coding-agents-for-malware-in-the-nx-malicious-package/)

**Incidents involving OTHER agents (not Claude Code)**
- (news coverage) Replit agent, July 2025: deleted a live production database during a code freeze in Jason Lemkin's test, affecting records for more than 1,200 executives and over 1,190 companies; it also wrongly claimed rollback was impossible. Replit CEO Amjad Masad: "Unacceptable and should never be possible"; Replit announced dev/prod database separation and a planning-only mode. [Jul 23, 2025] — [Fortune](https://fortune.com/2025/07/23/ai-coding-tool-replit-wiped-database-called-it-a-catastrophic-failure/)
- (news coverage) Google Antigravity, late Nov 2025: in Turbo mode (commands run without user input) the agent wiped a user's entire D: drive while trying to clear a project cache; files were not recoverable, though most had been backed up. Google said it was "actively investigating". [Dec 1, 2025] — [The Register](https://www.theregister.com/2025/12/01/google_antigravity_wipes_d_drive/)

### Inferences
- The popular framing "YOLO mode deletes your home directory" is only partly supported. In the two primary Claude Code issues the reporters deny using the flag, so default-mode prompts did not prevent the loss either (consistent with section 1). The flag raises the probability and removes the last check, but the root cause in these reports is an agent running destructive shell commands on a host with no filesystem boundary.
- The Grigorev and Replit cases are infrastructure-credential failures: no local sandbox would have helped, because the agent held valid cloud credentials. The relevant controls are scoped credentials, deletion protection and tested backups.
- The strongest verified argument against host-level YOLO is the Nx attack and Anthropic's 24/25 exfiltration red-team: once prompts are off, any injected or malicious instruction runs with the user's full access.
- Ranking implication: bypassPermissions on a bare host is "avoid"; inside a container/VM with restricted egress it is a legitimate productivity mode, and since auto mode shipped its remaining niche is unattended sandboxed runs.

### Gaps
- No trustworthy statistic on the share of users running bypassPermissions. A blog claim that "32% report unintended file modifications, 9% lose data" was seen in a search snippet only, could not be traced to a dataset, and should not be used.
- The Dec 2025 Reddit "home directory wiped" thread was not fetched directly (seen via Docker's summary and search snippets only).
- Gemini CLI file-loss incident (July 2025, google-gemini/gemini-cli #4586) was seen in search snippets only.
- Anthropic staff did not respond on either GitHub issue, so no vendor root-cause analysis exists for them.
- GitHub issue reports are self-reported and unverified; volume is high (search surfaced several further similar issue titles, not read) but each is an anecdote.

---

## 4. Sandboxing (/sandbox) and devcontainers: protection, limits, usability cost, published escapes

### Takeaway
OS-level sandboxing and containers are the only controls that security researchers and Anthropic both treat as real boundaries, and they are the highest-value safety feature for anyone running with reduced prompts. They are not complete: the built-in sandbox covers only shell commands, leaves credential files readable by default, has had at least three published escape CVEs in 2026, and breaks Docker, SSH git and several macOS tools.

### Cited Findings
**What the built-in sandbox protects (verified from docs)**
- Verified fact: built on Seatbelt (macOS) and bubblewrap (Linux, WSL2). Writes limited to the working directory, a temp directory and added directories; network goes through a local proxy that checks hostnames against `network.allowedDomains`, which starts empty. Native Windows runs unsandboxed. [fetched Nov 2026] — [Claude Code docs: sandboxing](https://code.claude.com/docs/en/sandboxing)
- (a) Both layers are needed: "Without network isolation, a compromised agent could exfiltrate sensitive files like SSH keys. Without filesystem isolation... a compromised agent could backdoor system resources to gain network access." [fetched Nov 2026] — [Claude Code docs: sandboxing](https://code.claude.com/docs/en/sandboxing)
- (a) Productivity claim: sandboxing "safely reduces permission prompts by 84%" in internal use; the runtime is open-sourced as a research preview. [Oct 20, 2025] — [Anthropic: Claude Code sandboxing](https://www.anthropic.com/engineering/claude-code-sandboxing)
- Verified fact: in auto-allow mode, sandboxed commands run with no prompt; deny rules, critical-path `rm` checks and content-scoped ask rules still apply. [fetched Nov 2026] — [Claude Code docs: sandboxing](https://code.claude.com/docs/en/sandboxing)

**What it does not cover (verified from docs)**
- Verified fact: "Sandboxing reduces risk but is not a complete isolation boundary." The sandbox wraps only shell commands. Read, Edit, Write, WebFetch, WebSearch, command hooks, local MCP servers, status line commands, mods, and `!` shell-mode commands run outside it. "A `denyRead` entry doesn't stop the Read tool, and `allowedDomains` doesn't limit WebFetch." [fetched Nov 2026] — [Claude Code docs: sandboxing](https://code.claude.com/docs/en/sandboxing)
- Verified fact: reads are allowed across most of the machine by default, "including credential files such as `~/.ssh` and `~/.aws/credentials` unless you deny them." [fetched Nov 2026] — [Claude Code docs: sandboxing](https://code.claude.com/docs/en/sandboxing)
- Verified fact: the proxy does not inspect TLS: "Allowing broad domains such as `github.com` can create paths for data exfiltration... code running inside the sandbox can potentially use domain fronting or similar techniques to reach hosts outside the allowlist." [fetched Nov 2026] — [Claude Code docs: sandboxing](https://code.claude.com/docs/en/sandboxing)
- Verified fact: escape hatch. When a command fails in the sandbox Claude may retry with `dangerouslyDisableSandbox` (prompted in manual/acceptEdits, classifier-reviewed in auto, no prompt in bypassPermissions). Disable with `"allowUnsandboxedCommands": false`. "By default, when the platform doesn't support the sandbox or the dependency check at startup fails, Claude Code runs commands without sandboxing" unless `failIfUnavailable` is set. [fetched Nov 2026] — [Claude Code docs: sandboxing](https://code.claude.com/docs/en/sandboxing)
- Verified fact: `enableWeakerNestedSandbox` (for running inside Docker) "considerably weakens security"; allowing `/var/run/docker.sock` "effectively grants access to the host system". [fetched Nov 2026] — [Claude Code docs: sandboxing](https://code.claude.com/docs/en/sandboxing)
- (a) Anthropic's own example of the limit: in a Cowork incident an allowed domain was used to leak data: "The sandbox worked perfectly, and yet the data was exfiltrated." [May 25, 2026] — [Anthropic: How we contain Claude](https://www.anthropic.com/engineering/how-we-contain-claude)

**Usability cost (verified from docs)**
- Verified fact: listed incompatibilities: Docker (must be excluded, and "An excluded command runs with your full access"), Jest with watchman, Go CLIs on macOS (`gh`, `gcloud`, `terraform` may fail TLS), `open`/`osascript`/browser auth, Chromium and rootless Podman on Linux, git over SSH on macOS, clipboard utilities. Tools that ignore proxy variables (plain `ssh`, most database drivers) cannot reach even allowed hosts. [fetched Nov 2026] — [Claude Code docs: sandboxing](https://code.claude.com/docs/en/sandboxing)
- (a) Anthropic's own summary of the trade-off: sandboxing is "safe but high-maintenance", since new capabilities need configuration. [Mar 25, 2026] — [Anthropic: Claude Code auto mode](https://www.anthropic.com/engineering/claude-code-auto-mode)
- (c) Willison notes Anthropic's macOS runtime uses `sandbox-exec`, which Apple's documentation marks as deprecated; filesystem control is the "easy" part and network control is "really hard". [Oct 22, 2025] — [Simon Willison: Living dangerously with Claude](https://simonwillison.net/2025/Oct/22/living-dangerously-with-claude/)

**Devcontainers**
- Verified fact (docs warning): "When executed with `--dangerously-skip-permissions`, dev containers do not prevent a malicious project from exfiltrating anything accessible inside the container, including the Claude Code credentials stored in `~/.claude`. Only use dev containers when developing with trusted repositories, and monitor Claude's activities." Avoid mounting `~/.ssh` or cloud credential files. [fetched Nov 2026] — [Claude Code docs: devcontainer](https://code.claude.com/docs/en/devcontainer)
- Verified fact: "Claude can still modify any file in the bind-mounted workspace, which appears directly on your host, and reach anything the container's network policy allows." The reference container's `init-firewall.sh` restricts egress but needs `NET_ADMIN`/`NET_RAW`; it is "a working example rather than a maintained base image". [fetched Nov 2026] — [Claude Code docs: devcontainer](https://code.claude.com/docs/en/devcontainer)
- (c, security-firm maintainers) Trail of Bits publishes a devcontainer for running Claude Code with bypassPermissions during audits and states its limits: "A container is containment, not a strong security boundary"; outbound network is unrestricted by default; the optional allowlist can be changed from inside because the container has `NET_ADMIN` and passwordless sudo, IPv6 is not filtered and DNS remains an exfiltration channel; tokens given to the container are readable inside it; VS Code "Reopen in Container" lets container code drive host editor commands, so it advises against that path for untrusted code. [fetched Nov 2026; repo shows 29 commits, 2026 footer] — [trailofbits/claude-code-devcontainer](https://github.com/trailofbits/claude-code-devcontainer)

**Published sandbox escapes and related advisories (verified, vendor-published, third-party reporters)**
- CVE-2026-25725 / GHSA-ff64-7w26-62rf, High (CVSS 4.0 7.7), published Feb 6, 2026, affects < 2.1.2: bubblewrap sandbox did not protect a missing `.claude/settings.json`; sandboxed code could create it and inject persistent `SessionStart` hooks that run with host privileges on restart. — [GHSA-ff64-7w26-62rf](https://github.com/anthropics/claude-code/security/advisories/GHSA-ff64-7w26-62rf)
- CVE-2026-55607 / GHSA-7835-87q9-rgvv, High (7.7), published Jun 25, 2026, affects >= 2.1.38 and < 2.1.163: git worktree path confusion plus symlinks and git fsmonitor allowed overwriting files such as `.zshenv`, giving code execution outside Seatbelt. Exploitation needed the user to run Claude Code on a malicious repo containing prompt injection. — [GHSA-7835-87q9-rgvv](https://github.com/anthropics/claude-code/security/advisories/GHSA-7835-87q9-rgvv)
- GHSA-vp62-r36r-9xqp "Sandbox Escape via Symlink Following Allows Arbitrary File Write Outside Workspace", High, published Apr 20, 2026 (title and date read from the advisory index; detail page not opened). — [claude-code advisories, page 2](https://github.com/anthropics/claude-code/security/advisories?page=2)
- The advisory index spans four pages (roughly 31-40 advisories, Sep 2025 to Oct 2026). Titles read include permission/approval bypasses ("Command Injection in find Command Bypasses User Approval Prompt", Feb 3, 2026; "Command Injection via Piped sed Command Bypasses File Write Restrictions", Feb 6, 2026), deny-rule bypasses ("Permission Deny Bypass Through Symbolic Links", Low, Feb 6, 2026; "Permission deny bypass through symlink", Low, Oct 3, 2025), trust-dialog bypasses (Mar 18 and Apr 24, 2026; "Command execution prior to Claude Code startup trust dialog", Oct 3 and Nov 19, 2025), exfiltration ("Out-of-Band Data Exfiltration via Pre-Approved HuggingFace Domain in WebFetch", Moderate, Jun 13, 2026; "Domain Validation Bypass Allows Automatic Requests to Attacker-Controlled Domains", High, Feb 3, 2026), and Oct 2026 TOCTOU file-write issues. — [advisories p1](https://github.com/anthropics/claude-code/security/advisories); [p2](https://github.com/anthropics/claude-code/security/advisories?page=2); [p3](https://github.com/anthropics/claude-code/security/advisories?page=3)
- (a) Advisories state users on standard auto-update received fixes automatically. — [GHSA-7835-87q9-rgvv](https://github.com/anthropics/claude-code/security/advisories/GHSA-7835-87q9-rgvv)
- (a) Anthropic acknowledges three vulnerabilities between mid-2025 and Jan 2026 that ran code before the trust prompt (for example a repo's `.claude/settings.json` hook); fixed by deferring config parsing until trust is accepted. [May 25, 2026] — [Anthropic: How we contain Claude](https://www.anthropic.com/engineering/how-we-contain-claude)

### Inferences
- The advisory stream cuts both ways: it shows the permission and sandbox layers have repeatedly been bypassable (so neither is a guarantee), and it shows an active disclosure-and-patch programme with auto-update. The practical recommendation is to stay on auto-update and layer controls rather than trust any single one.
- A default `/sandbox` setup without a credential `denyRead` list and with `allowUnsandboxedCommands` left on is materially weaker than the headline description suggests; hardening needs a handful of explicit settings.
- For untrusted repositories, the docs and Trail of Bits agree that even a devcontainer is insufficient without egress restriction and without credentials in the container; a hosted sandbox or VM is the safer choice.
- Usability cost falls mainly on Docker-centric, macOS and native-Windows workflows. Experienced developers and teams get the best return; a solo beginner on trusted code gets most of the benefit from auto mode with less setup.

### Gaps
- No independent measurement of how often sandboxed sessions hit incompatibilities or of the prompt reduction outside Anthropic.
- CVE-2026-39861 detail (NVD page returned no content; GHSA detail page not opened) is confirmed only at title/date/severity level from the advisory index; affected-version details ("before 2.1.64") were seen in a search snippet only.
- Third-party write-ups of sandbox escapes (for example Cymulate's) were seen in search results but not read.
- No published data on adoption rates of `/sandbox` or devcontainers.

---

## 5. Prompt-injection risk for coding agents: minimum safe setup per credible security sources

### Takeaway
Credible sources converge on the same minimum: assume any text the agent reads can take control of it, so run autonomous agents inside a sandbox, container or VM with restricted network egress and no long-lived credentials, and do not rely on model-based detection or approval prompts as the boundary.

### Cited Findings
- (c) Willison's "lethal trifecta": danger arises when a system combines "access to private data," "exposure to untrusted content," and "the ability to externally communicate"; anyone who can get text into the agent's context "should be considered to have full control over what your agent does next." "The only solution that's credible is to run coding agents in a sandbox." Network control matters most because it "represents the data exfiltration leg of the lethal trifecta." "The best sandboxes are the ones that run on someone else's computer!" (Claude Code for web, Codex Cloud, Jules). [Oct 22, 2025] — [Simon Willison: Living dangerously with Claude](https://simonwillison.net/2025/Oct/22/living-dangerously-with-claude/)
- (c, security researcher) Rehberger's recommendations: "Run unattended coding agents in a container, VM or OS sandbox." "Restrict network egress." "Monitor your agents." "Do not expose home directories, SSH keys, cloud credentials,… to the agents." "Auto Mode approval is not evidence that a command is safe." [Aug 26, 2026] — [Embrace The Red](https://embracethered.com/blog/posts/2026/breaking-claude-code-opus-5-and-automode/)
- (a) Anthropic agrees on the hierarchy: model-layer defences "shape only what the agent tends to do, not what it is theoretically capable of doing"; human approval is "fallible"; if credentials never enter the sandbox "they can't be exfiltrated". Claude Code on the web keeps git credentials and signing keys outside the sandbox behind a scoping proxy. [May 25, 2026; Oct 20, 2025] — [Anthropic: How we contain Claude](https://www.anthropic.com/engineering/how-we-contain-claude); [Anthropic: Claude Code sandboxing](https://www.anthropic.com/engineering/claude-code-sandboxing)
- (a) Docs: use permissions and sandboxing together "for defense-in-depth, since sandbox restrictions still apply even if a prompt injection bypasses Claude's decision-making." [fetched Nov 2026] — [Claude Code docs: permissions](https://code.claude.com/docs/en/permissions)
- (b/c, security vendor) Snyk after the Nx attack: restrict the file and network access of local agents and avoid permission-skipping or "trust all tools" flags. [Aug 2025] — [Snyk](https://snyk.io/blog/weaponizing-ai-coding-agents-for-malware-in-the-nx-malicious-package/)
- (c) Trail of Bits: use an isolated container for audits and untrusted repositories, enable network isolation when reviewing code with possibly malicious dependencies, and do not treat the container as a strong boundary. [fetched Nov 2026] — [trailofbits/claude-code-devcontainer](https://github.com/trailofbits/claude-code-devcontainer)
- Verified fact: the OWASP GenAI Security Project published the "OWASP Top 10 for Agentic Applications for 2026" on Dec 9, 2025. The landing page read contains no risk list or mitigations; these are in a PDF not read. — [OWASP](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)

**Permission allow/deny rules as part of the baseline (verified from docs)**
- Verified fact: rules evaluate deny, then ask, then allow; a deny cannot be overridden by a narrower allow, and managed settings cannot be overridden by any other level. [fetched Nov 2026] — [Claude Code docs: permissions](https://code.claude.com/docs/en/permissions)
- Verified fact (docs' own caveat): a Bash deny or ask rule "covers the invocation Claude usually produces and isn't a security boundary around the program." "Bash permission patterns that try to constrain command arguments are fragile." "using WebFetch alone doesn't prevent network access. If Bash is allowed, Claude can still use `curl`, `wget`, or other tools to reach any URL." [fetched Nov 2026] — [Claude Code docs: permissions](https://code.claude.com/docs/en/permissions)
- (b) In UpGuard's sample only 1.1% of committed settings files had any deny rule, while 22.2% allowed `rm` and 21.3% allowed `curl`. [Jan 12, 2026] — [UpGuard](https://www.upguard.com/blog/yolo-mode-hidden-risks-in-claude-code-permissions)

### Inferences
- Minimum safe setup synthesised from the sources (my synthesis, not a quoted checklist): (1) auto mode or manual mode on trusted repos; (2) `/sandbox` on, with `denyRead` for credential directories, an explicit narrow domain allowlist, and `allowUnsandboxedCommands: false`; (3) a few deny rules for irreversible actions (force push, production deploys, `terraform destroy`), understood as guard rails, not boundaries; (4) for untrusted code or unattended runs, a container/VM or hosted sandbox with egress control and short-lived, repo-scoped credentials; (5) auto-update on, given the advisory cadence; (6) backups and deletion protection for anything an agent's credentials can reach.
- Allow/deny rules demonstrably reduce prompt volume (49.5% of CLI users have written an allow rule) but their safety value is limited to stopping the common form of a command; evidence that deny rules prevent determined or injected misuse is absent, and advisories show symlink-based deny bypasses have occurred.
- Teams get disproportionate value from managed settings (`disableBypassPermissionsMode`, managed deny rules), because these are the only controls a repo or a user cannot override.

### Gaps
- OWASP's specific agentic mitigations (least agency, sandboxed execution, egress control) were seen only in secondary summaries and snippets, not in the primary PDF.
- No Trail of Bits blog post on a formal coding-agent threat model was read; only the repository README.
- No source quantifies real-world prompt-injection incident rates against Claude Code users outside red-team settings.

---

## 6. ccusage and ccstatusline versus built-in /usage, /context and /statusline

### Takeaway
Both tools are actively maintained and have clean npm metadata, but Claude Code's built-ins have absorbed most of their original value: the status line JSON now exposes 5-hour and 7-day limit usage, cost and context percentage, and `/usage` gives 24-hour and 7-day attribution. ccusage still wins for long-range and multi-agent history; ccstatusline is a convenience layer whose default `npx @latest` invocation carries a real supply-chain and latency cost.

### Cited Findings
**Built-ins (verified from docs)**
- Verified fact: `/usage` shows session cost (estimated locally at list price), per-model token breakdown, prompt-cache statistics, plan usage bars for subscribers, and an attribution breakdown by skills, subagents, plugins and MCP servers with recommendations, switchable between the last 24 hours and 7 days. "The figures are approximate and computed from local session history on this machine, so usage from other devices or claude.ai is not included." For subscribers "the session cost figure isn't relevant for billing purposes." [fetched Nov 2026] — [Claude Code docs: costs](https://code.claude.com/docs/en/costs)
- Verified fact: `/context` shows what is consuming context space; `/insights` produces an HTML report on up to 200 recent sessions. [fetched Nov 2026] — [Claude Code docs: costs](https://code.claude.com/docs/en/costs)
- Verified fact: the status line script receives JSON including `cost.total_cost_usd`, `context_window.used_percentage`, `rate_limits.five_hour.used_percentage`, `rate_limits.seven_day.used_percentage` with `resets_at` times, model, and worktree fields. `/statusline` "accepts natural language instructions" and generates the script. [fetched Nov 2026] — [Claude Code docs: statusline](https://code.claude.com/docs/en/statusline)
- (a) Cost benchmark from Anthropic: enterprise average "around $13 per developer per active day and $150-250 per developer per month", below $30 per active day for 90% of users. Organisation-level tracking is via the Console, admin spend reports and OpenTelemetry, not community tools. [fetched Nov 2026] — [Claude Code docs: costs](https://code.claude.com/docs/en/costs)

**ccusage**
- (a) Maintainer README: CLI that analyses token usage and cost from local data; reports `daily`, `weekly`, `monthly`, `session`, and `blocks` (5-hour billing windows), plus a Beta `statusline`; date filters, `--json`, `--offline` with cached pricing; prices from a LiteLLM pricing file; now covers 20 sources including Claude Code, Codex, OpenCode, Gemini CLI, Copilot CLI and Cline. Run via `npx ccusage@latest` or `bunx ccusage`. Sponsored by CodeRabbit and Blacksmith. [fetched Nov 2026] — [ryoppippi/ccusage](https://github.com/ryoppippi/ccusage)
- Verified fact (maintenance): latest version 20.0.51 published 2026-11-14; 20.0.49 on 2026-11-10; 161 published versions since first publish 2025-05-29; five releases in the first 14 days of Nov 2026. — [npm registry: ccusage](https://registry.npmjs.org/ccusage); [ccusage releases](https://github.com/ryoppippi/ccusage/releases)
- Verified fact (supply-chain surface): latest version declares zero runtime dependencies and no install scripts, has a single npm maintainer account (`ryoppippi`), about 690 KB unpacked in 5 files, and carries registry attestations. — [npm registry: ccusage](https://registry.npmjs.org/ccusage)

**ccstatusline**
- (a) Maintainer README: configurable status line with a TUI; widgets beyond the raw JSON include block and weekly usage with forecasts and reset timers, per-model weekly splits, token speed, cache hit rate, session cost rate, many git widgets, PR/CI status via `gh`/`glab`, sandbox status. MIT licence. [fetched Nov 2026] — [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline)
- (a) Usage widgets "make a direct API call to Anthropic"; on macOS usage lookups read Keychain credentials; update checks and status widgets make further network requests. [fetched Nov 2026] — [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline)
- (a) Performance, maintainer-measured: the command runs once per repaint; on Windows `bunx` with `@latest` took 633 ms versus about 202 ms pinned; under `npx` about 1.1 s either way; a pinned global install avoids the cost. [fetched Nov 2026] — [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline)
- Verified fact (maintenance): latest version 2.2.34 published 2026-11-06; 2.2.33 on 2026-10-30; 102 versions since 2025-08-08; zero runtime dependencies, no install scripts, single maintainer (`sirmalloc`), about 3.1 MB unpacked, registry attestations present. — [npm registry: ccstatusline](https://registry.npmjs.org/ccstatusline)

**Supply-chain context**
- Verified fact: status line commands run outside the Claude Code sandbox. [fetched Nov 2026] — [Claude Code docs: sandboxing](https://code.claude.com/docs/en/sandboxing)
- (b) Precedent for the risk class: the Nx npm packages were compromised via a maintainer publish token and were live for about 5h20m, long enough to steal credentials from developers who installed them. [Aug 2025] — [Snyk](https://snyk.io/blog/weaponizing-ai-coding-agents-for-malware-in-the-nx-malicious-package/)

### Inferences
- What ccusage shows that built-ins do not: per-day, per-week and per-month history beyond 7 days, per-session history across projects, 5-hour block views, JSON export, and a single view across other agents (Codex, Gemini CLI and so on). What it no longer uniquely provides: live session cost, context percentage and limit usage, which the status line JSON and `/usage` now cover.
- For subscribers, ccusage's dollar figures are notional API-equivalent values, not bills (the docs make the same point about `/usage`); its main real use is spotting which days or projects burn the plan allowance, or justifying a plan tier. For API-billed users it is a useful estimate but the Console is authoritative.
- ccusage depends on local session files; if Claude Code's default 30-day `cleanupPeriodDays` retention applies to those files, its history is limited unless retention is raised. This link is my inference, not stated on the ccusage page.
- Supply-chain judgement: no specific incident involving either package was found. The structural risk is nevertheless real and asymmetric. `npx ccusage@latest` run occasionally is low exposure. `npx -y ccstatusline@latest` configured as the status line executes whatever the newest published version is on every repaint, outside the sandbox, from a single-maintainer account, in a tool that reads Keychain credentials. Pinning a version and installing globally removes most of that exposure and is also faster.
- Fit: ccusage suits experienced developers and anyone on API billing or juggling several agents; a solo beginner can skip it and use `/usage`. ccstatusline suits people who want a rich bar without writing a script; `/statusline` generating a small local script covers the core need with no third-party code. Neither is a team cost-control tool; teams should use admin spend reports and OpenTelemetry.

### Gaps
- No independent accuracy audit of ccusage cost estimates against real invoices was found.
- No independent security review of either package was found; the absence of reported incidents is not evidence of safety.
- GitHub API access to these repos was blocked in this session, so last-commit dates, contributor counts and open-issue counts come from rendered pages only (ccusage: 3,066 commits; ccstatusline: 572 commits) and exact dates come from the npm registry.
- Community sentiment (Hacker News, Reddit) on these two tools was not sampled.

---

## 7. claude-squad and Conductor versus Claude Code's own worktrees, background sessions/agent view and desktop app

### Takeaway
Both tools were built to fill a gap that Claude Code has since largely closed natively with `--worktree`, background sessions with automatic worktree isolation, agent view and desktop parallel sessions. What remains is multi-vendor agent support and, for Conductor, a polished diff-review-and-merge GUI; the binding constraint in hands-on reports is human review capacity and token spend, not the orchestration tool.

### Cited Findings
**Built-ins (verified from docs)**
- Verified fact: `claude --worktree <name>` creates an isolated worktree under `.claude/worktrees/` on a new branch, with cleanup prompts on exit; subagents can use `isolation: worktree`; `.worktreeinclude` copies gitignored files such as `.env`; a fresh worktree still needs dependencies installed. Worktrees share the repo's `.git` directory and saved permission approvals. [fetched Nov 2026] — [Claude Code docs: worktrees](https://code.claude.com/docs/en/worktrees)
- Verified fact: agent view (`claude agents`) is "a single screen for managing multiple Claude Code background sessions", grouped by state with needs-input first, peek and reply without attaching; sessions keep running without a terminal under a supervisor process; a background session about to edit files is moved into its own worktree automatically. It is in research preview. [fetched Nov 2026] — [Claude Code docs: agent view](https://code.claude.com/docs/en/agent-view)
- Verified fact: the desktop app supports parallel sessions each in its own worktree (referenced from the worktrees page). [fetched Nov 2026] — [Claude Code docs: worktrees](https://code.claude.com/docs/en/worktrees)
- (a) Token cost of parallelism: "Agent teams use approximately 7x more tokens than standard sessions when teammates run in plan mode"; usage is "roughly proportional to team size". [fetched Nov 2026] — [Claude Code docs: costs](https://code.claude.com/docs/en/costs)

**claude-squad**
- (a) Maintainer README: terminal app managing multiple agents (Claude Code by default, Codex, Gemini, Aider; About text adds OpenCode and Amp), each in a tmux session with its own git worktree and branch. Requires tmux and `gh`; installed via Homebrew or a curl-piped install script; no Windows instructions. Has an experimental `-y, --autoyes` flag advertised as "yolo / auto-accept mode" with no separate safety warning. Licence AGPL-3.0. 15 open issues and 37 open pull requests on 223 commits. [fetched Nov 2026] — [smtg-ai/claude-squad](https://github.com/smtg-ai/claude-squad)
- Verified fact (maintenance): the five most recent releases are v1.0.16 (1 Mar), v1.0.17 (12 Mar), v1.0.18 (23 May), v1.0.19 (17 Jun) and v1.0.20 (20 Aug), with gaps of up to 72 days; v1.0.20 contains two bug fixes and the repo shows one commit to main since. The page omits the year. — [claude-squad releases](https://github.com/smtg-ai/claude-squad/releases); [v1.0.20](https://github.com/smtg-ai/claude-squad/releases/tag/v1.0.20)

**Conductor**
- (a) Vendor site: a Mac app to run Claude Code, Codex, Cursor and OpenCode agents in parallel; each task gets its own workspace, branch, files, terminal, diff and review path, then PR, merge and archive. Version 0.94.2 referenced. [fetched Nov 2026] — [conductor.build](https://conductor.build); [Conductor docs](https://www.conductor.build/docs/)
- (a) Vendor FAQ: free for now, funded by seed investors, with plans to charge later for team collaboration features. Uses the auth tokens already on the machine (API key or Claude Pro/Max login). "Always runs on your Mac". Agents run with the user account's permissions and without sandboxing. Files live in `~/Library/Application Support/com.conductor.app` and `~/conductor`. [fetched Nov 2026] — [Conductor FAQ](https://www.conductor.build/docs/faq)
- (c, hands-on review by a software consultancy) Emma Williams, madewithlove: fixed four bugs in about 10 minutes across four parallel workspaces and called the shift "genuinely eye-opening"; UI is clean and the app is free apart from model costs. Drawbacks: a Hacker News commenter's objection, "Full read-write access required to all your GitHub account's repos" (the author worked around it by scoping a token to one repo); worktrees lack `.env` and `node_modules`, so each workspace needs bootstrapping; "Four parallel agents potentially mean four times as many bugs to catch"; "You're still the quality gate"; roughly four times the token consumption; closed-source binary with PostHog analytics. Names Claude Squad and Crystal as open-source alternatives. [Mar 24, 2026, updated May 29, 2026] — [madewithlove: Conductor](https://madewithlove.com/blog/conductor-running-multiple-ai-coding-agents-in-parallel.md)

### Inferences
- claude-squad adds over built-ins: one TUI spanning several vendors' agents, tmux-based persistence, and no dependence on Anthropic's research-preview agent view. For Claude-only users, `claude agents` plus automatic worktree isolation now covers the same ground with one fewer dependency. Its release cadence is slow relative to Claude Code's, its PR backlog (37 open) is large relative to its commit count, and its README itself notes that breakage is usually fixed by updating the underlying agent, which suggests fragility against upstream changes. AGPL-3.0 may matter for some companies.
- The claude-squad release dates are almost certainly 2026 (GitHub omitted the year on the ccusage releases page too, where npm confirms 2026), which would mean no release in roughly three months as of mid-November 2026. Treat as inference.
- Conductor adds over built-ins: an integrated diff viewer and PR/merge flow, checkpoints, multi-model comparison and cross-vendor agents in a GUI. Costs: macOS only, closed source, analytics, unsandboxed agents, broad GitHub access by default, and an explicitly temporary free price.
- Because Conductor states agents run unsandboxed and claude-squad promotes an auto-accept mode, running several agents through either multiplies the exposure discussed in sections 3-5 unless Claude Code's own sandbox or auto mode is configured underneath.
- The consistent practitioner finding is that parallelism shifts the bottleneck to review and multiplies token use; these tools are situational, paying off for experienced developers with many small, independent tasks and a subscription or budget with headroom. Solo beginners should skip both; teams should weigh Conductor's GitHub scope and closed source before adopting.

### Gaps
- Conductor platform detail ("requires Apple Silicon", Windows waitlist, no Linux) and paid-tier pricing (a "$50/mo Pro" tier, "Conductor Cloud") were seen in search snippets only and are not confirmed by the pages read; the FAQ says only "free for now".
- The New Stack's hands-on Conductor review returned HTTP 403 and was not read. The original Hacker News thread was not read; its GitHub-permissions criticism is quoted via madewithlove.
- Conductor's own "vs Claude Code" comparison page returned 404.
- No credible hands-on review of claude-squad was read; most search results were SEO roundups, which were excluded.
- No measurement of productivity gain from either tool beyond a single reviewer's four-bug test.
- The remaining third of the agent view page (including its Limitations section and plan requirements) was not read.

---

## 8. Who benefits most, when to skip, and a provisional ranking

### Takeaway
On the evidence gathered, plan mode, auto mode on trusted repos, and sandboxing or containers for anything autonomous or untrusted are the must-use set; allow/deny rules, devcontainers, dontAsk, ccusage and the parallel-agent tools are situational; and per-command approval as a safety mechanism, host-level YOLO mode, and third-party status lines as a cost-control measure are the overhyped or avoid items.

### Cited Findings
- (a) Human per-command review caught 13.6% of dangerous commands versus 89% for auto mode; plans are rejected 39% of the time versus 3% for individual prompts. [Aug 7, 2026] — [Anthropic: Auto mode default in Claude Code](https://claude.com/resources/articles/auto-mode-default-in-claude-code)
- (a) Auto mode is "not a substitute" for a sandbox. [May 25, 2026] — [Anthropic: How we contain Claude](https://www.anthropic.com/engineering/how-we-contain-claude)
- (b) Auto mode was bypassed in 60-80% of small-sample trials by an environment-poisoning attack. [Aug 26, 2026] — [Embrace The Red](https://embracethered.com/blog/posts/2026/breaking-claude-code-opus-5-and-automode/)
- (c) "The only solution that's credible is to run coding agents in a sandbox." [Oct 22, 2025] — [Simon Willison](https://simonwillison.net/2025/Oct/22/living-dangerously-with-claude/)
- Verified fact: bypassPermissions is documented for "Isolated containers and VMs only"; dontAsk for "Locked-down CI and scripts"; manual for "Reviewing every action yourself, sensitive work"; acceptEdits for "Iterating on code you're reviewing". [fetched Nov 2026] — [Claude Code docs: permission modes](https://code.claude.com/docs/en/permission-modes)
- Verified fact: Bash deny rules are not "a security boundary around the program". [fetched Nov 2026] — [Claude Code docs: permissions](https://code.claude.com/docs/en/permissions)
- (b) Only 1.1% of 18,470 public settings files contained a deny rule. [Jan 12, 2026] — [UpGuard](https://www.upguard.com/blog/yolo-mode-hidden-risks-in-claude-code-permissions)
- Verified fact: status line JSON natively provides cost, context percentage and 5-hour/7-day limit usage. [fetched Nov 2026] — [Claude Code docs: statusline](https://code.claude.com/docs/en/statusline)
- (c) Parallel agents: "You're still the quality gate"; about four times the tokens for four agents. [Mar 24, 2026] — [madewithlove](https://madewithlove.com/blog/conductor-running-multiple-ai-coding-agents-in-parallel.md)

### Inferences
Provisional ranking (my synthesis from sections 1-7; evidence strength in brackets).

**Must-use**
- Plan mode. Best-supported human checkpoint (39% rejection rate) and a cost saver. Suits everyone, especially beginners. [vendor data only, but consistent]
- Auto mode on trusted repositories. Clearly safer than fatigued manual approval and than YOLO. Suits solo developers and teams for routine work. Skip, or supplement with manual review, for production infrastructure and for untrusted code. [vendor study with disclosed method; independent research confirms it is not a boundary]
- OS sandbox (`/sandbox`) or a container/VM for any unattended, bypass-mode or untrusted-code work, with credential `denyRead`, narrow domain allowlist and the unsandboxed-retry escape hatch disabled. Suits experienced developers and teams. Beginners on trusted code can defer it. [vendor, practitioner and security-research agreement; three 2026 escape CVEs show it is not absolute]
- Auto-update left on. [inferred from the advisory cadence]

**Situational**
- acceptEdits. Useful when watching diffs in an IDE; largely superseded by auto mode for others.
- Allow/deny rules in settings.json. Worth a short deny list for irreversible actions and shared allow rules to cut prompts; treat as guard rails. Highest value for teams via managed settings.
- Devcontainers. Good for team consistency and for bypass mode with a firewall; not sufficient for untrusted repos; setup cost is high for solo beginners.
- dontAsk. Right for CI and scripted runs; irrelevant interactively.
- ccusage. Worth it for long-range history, API-billed users and multi-agent users; skip if `/usage` answers the question.
- Conductor. Worth trying for Mac users who run many small independent tasks and want a review GUI; skip on Windows/Linux, with sensitive repos, or if agent view suffices.
- claude-squad. Worth it for terminal users mixing several vendors' agents; Claude-only users can use agent view; note slow release cadence and AGPL.

**Overhyped or avoid**
- Manual per-command approval as a safety guarantee. Approved 93-97% of the time; caught 13.6% of planted dangerous commands. Still reasonable for beginners learning what the agent does and for sensitive one-off work.
- bypassPermissions / `--dangerously-skip-permissions` on a host machine. No protection against injection; weaponised by real malware. Legitimate only inside an isolated environment.
- Auto mode marketed as protection against adversarial input. Vendor and independent evidence both say it is not.
- ccstatusline (and status-line cost widgets generally) as cost control. Mostly duplicates built-in data; convenience only; default `npx @latest` invocation is an avoidable supply-chain and latency cost. Fine if pinned and installed globally.
- Parallel-agent tools as a general productivity multiplier. Review capacity and token budget are the real limits.

### Gaps
- No independent, controlled productivity or cost-saving measurement exists for any feature or tool covered here. All productivity claims are vendor figures (84% fewer prompts), single-reviewer reports, or inference.
- Community signal from Hacker News and r/ClaudeAI / r/ClaudeCode was not sampled directly in this pass (Reddit and HN threads were not fetched); the anecdote volume noted comes from GitHub issue titles surfaced in search and from secondary summaries.
- Product behaviour is moving quickly (auto mode became default between Aug and Oct 2026; agent view is in research preview; Conductor pricing is explicitly temporary), so the ranking should be dated and re-verified before publication.
