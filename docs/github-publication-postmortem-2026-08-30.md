# GitHub publication postmortem and runbook

Date: 30 August 2026

Incident: publication of the audited source survivors and Conjectures 395–409

Final outcome: resolved without data loss. Pull request 3 was merged into
`main` as `bc9514dff414eb210b2d3aaccfb2f479c772b7d2`. Its tree
`28e1f827787444f5a6b214f25e24bc868f9a1341` is exactly the locally verified
final tree. Pull request 2 was closed unmerged as obsolete.

## Executive diagnosis

The publication appeared stuck for several independent reasons. No single
GitHub outage or merge conflict was responsible.

| Symptom | Actual cause | Effect | Resolution |
|---|---|---|---|
| The final work existed in pull requests but not on `main`. | The delivery contract had not distinguished “open a PR” from “merge to `main`.” The conservative workflow stopped after preparing PR 3. | The technical work was complete, but the requested final repository state was not. | After explicit direction, verify the immutable PR head and merge it; future tasks must declare the delivery mode before publication. |
| PR 3 did not initially look like a self-contained final change. | It was opened as a stacked PR whose base was the PR 2 branch. PR 2 still contained a provisional LQG admission later withdrawn. | Review and merge state depended on two PRs, and the obsolete claim remained visible. | Put the complete corrected state on the PR 3 branch, retarget PR 3 to `main`, verify its merge base, then close PR 2 with a supersession note. |
| Local and remote commit SHAs disagreed even when the files agreed. | Local commits and GitHub Git-Data-API commits had different metadata and parent SHAs. Git commit identity includes those fields. | SHA comparison falsely suggested content divergence. | Compare tree and blob SHAs. The local and remote final trees both equalled `28e1f827...`. Fetch the remote commits immediately after API publication. |
| The first staging command rejected all three PDFs. | Sparse checkout explicitly excluded `paper/*.pdf`. Ordinary `git add` refuses paths outside the sparse definition. | The source could have been committed without its regenerated PDFs. | Stage explicit excluded paths with `git add --sparse`; stage a removed path with `git add --sparse -u <directory>`. |
| Initial large blob uploads had the wrong SHA. | Shell-output capture truncated base64 at 1,048,606 characters. This affected large TeX/web files and would affect PDFs. | The first uploaded objects were incomplete, although no branch referenced them. | Read files in 600,000-byte chunks, concatenate their base64, and require the returned GitHub blob SHA to equal `git hash-object <file>` before creating a tree. |
| A PR metadata update was rejected. | The update unnecessarily included `maintainer_can_modify: true`, which is a persistent permission change and was not authorized. | The retarget/title/body update did not execute on that attempt. | Retry with only the necessary metadata fields. Never bundle permission changes into routine PR edits. |
| Initial PR reads appeared empty. | Connector methods return different response envelopes. Early parsing assumed a `.structuredContent.result` wrapper even when fields were directly under `.structuredContent`. | Valid GitHub data was displayed as `{}`, making the remote state look unavailable. | Check `isError`, inspect the documented result shape for the exact method, and fail closed when required fields are absent. |
| `git fetch` worked but `git push` requested unavailable credentials. | The repository is publicly readable over ordinary Git transport, but authenticated writes are supplied only through the GitHub connector in this workspace. | A normal branch push could not publish despite successful fetches. | Choose the write transport explicitly. Use authenticated Git only when configured; otherwise use the connector's Git Data operations and verify every object. Never extract or repurpose connector credentials. |
| PR 3 briefly reported `mergeable: false` after retargeting. | GitHub was asynchronously recomputing mergeability after the base change. | A transient response looked like a conflict. | Re-fetch PR metadata and compare base/head. The next read reported `mergeable: true`, zero commits behind, and the expected merge base. |
| The PR showed 16 changed files although the consolidation commit touched 17 paths. | PR statistics are the net diff against `main`. The deleted temporary LQG verifier had only existed on the stacked branch, so its addition and deletion cancelled out. | The count looked inconsistent but the tree was correct. | Validate named paths and final tree identity, not a raw changed-file count from a different comparison base. |
| Local `main` remained stale after the connector merge. | GitHub API mutation does not update local Git refs. | The remote was correct while the workspace still displayed the old `main`. | `git fetch origin main <feature>`; then fast-forward or reset the clean local `main` ref to `origin/main` and switch to it. |

No malformed blob, incomplete PDF, or withdrawn conjecture reached `main`.
The incorrect intermediate blobs were unreferenced Git objects and therefore
had no repository effect.

## What happened, in order

1. The source-candidate audit was published as PR 2.
2. The fifteen-conjecture addition was published as PR 3, stacked on the PR 2
   branch rather than directly on `main`.
3. Independent re-audit changed the accepted source slate: candidate 10 became
   a strengthening of Conjecture 392 and the provisional LQG conjecture was
   removed. The final numbering became 394 and 395–409, not 394–410.
4. A consolidation commit made the PR 3 branch contain the complete corrected
   state. Its local and remote commits had different SHAs but the same tree.
5. Sparse-checkout and large-file transport required special handling before
   every source, verifier, and regenerated PDF was represented correctly on
   GitHub.
6. PR 3 was retargeted to `main`; PR 2 was marked superseded and closed.
7. The first handoff left PR 3 open. After the requested final-state
   clarification, its exact head `ef31d9b5ae637f348473588f03c6f641ac86b169`
   was merged with expected-head protection.
8. GitHub `main`, `origin/main`, and local `main` were then synchronized at
   merge commit `bc9514dff414eb210b2d3aaccfb2f479c772b7d2`.

## Root causes

### 1. The publication target was underspecified

“Include in the project” can mean either prepare a reviewable PR or complete a
merge. Those have different authorization and risk profiles. The workflow
correctly avoided an unrequested merge at first, but the final report did not
make the unmerged state prominent enough, so completion was perceived when
only PR preparation had completed.

Every future publication task must record one of these before the GitHub write
phase:

- `PR_ONLY`: open or update a PR; `main` will remain unchanged.
- `MERGE_TO_MAIN`: validate and merge the exact reviewed head, then verify
  `main` and synchronize the workspace.

If the request is ambiguous, ask once before publication. Every handoff must
say either “merged into `main` at SHA …” or “PR open; `main` unchanged.”

### 2. The final PR was stacked on a mutable, later-obsolete PR

Stacking was useful while the two batches were being developed separately,
but it was a poor final topology after the source slate changed. A final PR
must be self-contained against its intended merge base.

For a stacked workflow, use the stack only during iteration. Before final
review:

1. consolidate every accepted parent change onto the final branch;
2. retarget the final PR to `main`;
3. verify `merge_base == current main`, `behind_by == 0`, and the complete net
   file list;
4. close or clearly supersede obsolete parent PRs.

### 3. Commit identity was confused with content identity

The corresponding local and remote histories were:

| Stage | Local commit | Remote commit |
|---|---|---|
| source audit | `c9c939a` | `87e3e16` |
| graph-state programme | `d1751b2` | `9d90e74` |
| final corrections | `138a088` | `ef31d9b` |

The SHAs differ because the commits were created in different systems with
different parent identities and metadata. Their final tree was identical.

When GitHub objects are created through an API, use this hierarchy of checks:

1. each returned blob SHA equals the local `git hash-object` result;
2. the returned tree SHA equals the local final tree SHA;
3. the remote commit points to that tree and the expected remote parent;
4. the branch ref points to that remote commit.

Do not require a remote commit SHA to equal a separately created local commit
SHA. Prefer normal `git push` only when authenticated Git transport is already
configured and appropriate. If connector Git Data operations are required,
fetch the remote branch immediately and treat its commit history as canonical.

### 4. Sparse checkout hid a tracked-artifact staging rule

This workspace's sparse specification contains:

```text
/*
!/paper/*.pdf
```

The PDF files are available for generation and inspection but excluded from
ordinary sparse staging. Use explicit staging and inspect the staged tree:

```bash
git add --sparse paper/conjectures.pdf \
  paper/conjectures_blind.pdf paper/conjectures_skeleton.pdf
git add --sparse <other explicit paths>
git add --sparse -u verify
git diff --cached --check
git diff --cached --stat
```

Never infer that generated tracked artifacts were staged merely because they
appear in `git status`.

### 5. Large-file transport crossed an output boundary

The GitHub blob API accepts base64, but the intermediate shell-output channel
truncated large base64 strings. The observed truncated length was 1,048,606
characters. An incomplete upload still produces a valid Git blob, so success
from `create_blob` alone is not enough.

The safe procedure used here was:

1. split the raw file into 600,000-byte chunks;
2. make every non-final raw chunk a multiple of three bytes so concatenated
   base64 has no intermediate padding;
3. concatenate base64 chunks in order;
4. create the GitHub blob;
5. compare its returned SHA with `git hash-object <path>`;
6. do not create or move a tree/ref unless every comparison passes.

The three PDF blob SHAs verified in this incident were:

| File | Blob SHA |
|---|---|
| `paper/conjectures.pdf` | `701af7c149a309068394ea409a1cdfbb55225945` |
| `paper/conjectures_blind.pdf` | `bc11ca349395955e59aed0ec69d708b6a53a92e2` |
| `paper/conjectures_skeleton.pdf` | `b3f55bc119c5a3612facfb1954931642b3c6e456` |

### 6. Unnecessary mutation fields increased risk

The PR update needed only `base_branch`, `title`, `body`, and `state`. Adding
`maintainer_can_modify` changed a persistent repository permission and caused
the operation to be rejected. Mutation payloads should be minimal: omit every
field that is not required for the requested state transition.

### 7. GitHub has eventually consistent status fields

Immediately after retargeting, mergeability can be unknown or temporarily
false while GitHub recomputes the test merge. Do not force a merge or rewrite
history in response to the first status sample.

Instead:

1. fetch the PR again;
2. compare base and head explicitly;
3. confirm the head SHA has not moved;
4. wait for a stable `mergeable: true` result;
5. merge with `expected_head_sha` populated.

An empty combined-status or workflow-run list means this repository has no
reported checks for that commit; it is not a pending check. Local validation
therefore remains mandatory.

### 8. Connector response envelopes were not uniform

The GitHub methods used in this incident did not all expose fields at the same
nesting level. For example, PR metadata, created-blob SHAs, generic fetched
JSON, and comparison results required method-specific extraction. A permissive
fallback parser initially converted a successful PR read into an empty object.

For every connector call:

1. check `isError` before reading any payload;
2. follow the declared schema for that exact method;
3. require critical fields such as `head_sha`, `base_sha`, `sha`, and
   `merged` rather than replacing their absence with an empty object;
4. stop before any dependent write if a required field is absent;
5. log only the compact fields needed for verification, not an entire tool
   registry or oversized diff.

Successful transport is not the same as a complete semantic result. A missing
expected field must be treated as an error, not as an empty GitHub state.

### 9. Readable Git transport did not imply writable Git transport

This public repository could be fetched without authentication, which made the
shell Git remote look fully usable. A later push failed with `could not read
Username for 'https://github.com'`: the shell process had no write credential.
The authenticated GitHub connector is a separate authorization path.

Before choosing a publication mechanism:

1. distinguish public read access from authenticated write access;
2. prefer an already configured noninteractive Git credential when one exists;
3. otherwise use the connector's create-blob, create-tree, create-commit, and
   update-ref operations with object-hash verification;
4. never inspect, export, or repurpose connector credentials for shell Git;
5. after connector writes, use ordinary `git fetch` to synchronize the public
   objects and refs locally.

A failed unauthenticated push is a transport-selection error, not evidence that
the remote branch or repository is corrupt.

## Publication runbook

### Phase A: define completion

- Record `PR_ONLY` or `MERGE_TO_MAIN`.
- Record the repository, target branch, feature branch, and expected files.
- Choose the write transport: authenticated Git or authenticated connector.
- Identify whether regenerated binaries are tracked.
- If multiple PRs are stacked, name the one final PR that will become
  self-contained.

### Phase B: freeze and validate locally

- Finish independent review before the publication commit.
- Run all scoped verification programs.
- Compile every tracked document variant.
- Render and inspect affected pages.
- Check numbering, citations, references, and counts.
- Run `git diff --check` against the intended base, not only against the last
  local commit.
- Inspect sparse-checkout rules before staging.
- Require a clean working tree after committing.

### Phase C: establish the remote base

- Read the live `main` ref immediately before creating the remote commit.
- Read the live feature ref, if it exists.
- Validate each connector response against that method's declared schema.
- For a final PR, require the merge base to be current `main`.
- Never use a cached PR head or base SHA for a destructive mutation.

### Phase D: publish exact objects

- Upload text and binary blobs.
- Chunk any file that can cross the transport-output limit.
- Compare every returned blob SHA to `git hash-object`.
- Build the new tree from the live remote base tree.
- Require the returned tree SHA to equal the local final tree SHA.
- Create the commit with the expected remote parent.
- Move the feature ref without force unless a separately authorized history
  rewrite is intended.

### Phase E: normalize the PR

- Make the final PR self-contained against `main`.
- Use a minimal PR update payload; do not change permissions incidentally.
- Close obsolete PRs only after the replacement PR contains their surviving
  content.
- Re-fetch after retargeting; allow mergeability to recalculate.
- Compare the PR against `main` and interpret changed-file counts as net diffs.

### Phase F: merge safely

For `MERGE_TO_MAIN` only:

- require `base == main`;
- require `behind_by == 0`;
- require the expected head SHA;
- require stable mergeability and no failing required checks;
- merge using `expected_head_sha` so a late push aborts rather than silently
  changing the reviewed content.

### Phase G: verify the final state

After GitHub reports success, independently verify all of the following:

- the PR is closed and `merged == true`;
- `refs/heads/main` equals the reported merge commit;
- the merge commit has the expected parents;
- its tree equals the previously verified final tree;
- selected critical files on `main` have their expected blob SHAs;
- withdrawn files return 404 on `main`;
- local `origin/main` is refreshed;
- local `main` equals `origin/main` and the workspace is clean;
- the smoke verification suite passes on checked-out `main`.

Never force-move a dirty or checked-out local branch. If local `main` has
unpublished work, stop and reconcile it explicitly rather than treating ref
synchronization as housekeeping.

## Compact release checklist

Copy this block into future publication notes.

```text
[ ] Delivery mode is PR_ONLY or MERGE_TO_MAIN.
[ ] Write transport is explicitly authenticated for this workspace.
[ ] Final PR is self-contained against current main.
[ ] Independent review is frozen and recorded.
[ ] Tests, builds, rendering, citations, and numbering pass.
[ ] Sparse-checkout exclusions were handled explicitly.
[ ] Every remote blob SHA equals git hash-object(path).
[ ] Remote tree SHA equals the local final tree SHA.
[ ] PR base/head/merge-base were re-read from GitHub.
[ ] Every connector response supplied its required schema fields.
[ ] PR update payload contains no unrelated permission changes.
[ ] Mergeability was re-polled after any base change.
[ ] Merge uses expected_head_sha.
[ ] Remote main ref and merge tree were independently re-read.
[ ] Obsolete PRs and withdrawn files were checked.
[ ] Local main was fetched, synchronized, and smoke-tested.
[ ] Handoff explicitly says either “merged at SHA” or “main unchanged.”
```

## Incident verification record

The final checks for this incident were:

- PR 3: closed and merged;
- merge commit: `bc9514dff414eb210b2d3aaccfb2f479c772b7d2`;
- final tree: `28e1f827787444f5a6b214f25e24bc868f9a1341`;
- remote and local `main`: identical;
- `README.md`: 409 conjectures in 28 parts;
- combined audit: candidate 3 as Conjecture 394, candidate 10 strengthening
  Conjecture 392, and fifteen new Conjectures 395–409;
- obsolete `verify/ar_random_barcode_lqg.py`: absent from `main`;
- hybrid verifier: 7/7 checks passed;
- lazy-walk and cut-rank verifiers: passed;
- GitHub-reported workflow runs: none configured for these commits.
