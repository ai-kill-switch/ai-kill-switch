# AI Kill Switch – User Experience Goals

## Core Principles
- **Minimal effort**: A few lines are enough to integrate.  
- **Out of the box**: Essential components provided, ready to use.  
- **Extendable**: Domain-specific safety logic can be added easily.  
- **Controllable**: Real-time monitoring, safety management, and manual kill switch.  
- **Open**: Fully open source, transparent, and developer-friendly.  

## Developer Experience
- Add the SDK and mark points in the AI app.  
- Events are automatically observed and sent to the server.  
- Define custom safety logic only when needed.  

## Operator Experience
- Use the Kill Switch Dashboard to monitor AI behavior in real time.  
- Toggle safety logic or adjust parameters without redeployment.  
- Trigger the manual kill switch in case of emergencies.  

## AI Service User Experience
- Aware that the AI Kill Switch is running.
- Feel comfortable knowing the hidden AI is monitored and protected.

## Example Workflow
1. **Integrate SDK with a few lines of code**

    ```python
    from ai_kill_switch import ks, observe

    ks.init(server_url="http://localhost:8080")

    @observe(event="llm.infer")
    def infer(prompt):
        return llm(prompt)
    ```

2. **Define your own safety logic simply**

    ```python
    from ai_kill_switch import BaseKillerRule, KillSwitchSignal

    class MySafetyLogic(BaseKillerRule):
        def evaluate(self, event):
            if "toxic" in event.payload.get("response", ""):
                return KillSwitchSignal.block("toxic content detected")
            return KillSwitchSignal.allow()
    ```

3. **Start the server and open the Kill Switch Dashboard**

    ```bash
    docker compose up
    # Dashboard available at http://localhost:3000
    ```

4. **Observe and Control**  
   Data flows into the Kill Switch Dashboard automatically,  
   safety logic is applied for automatic analysis and control,  
   and operators can trigger a manual kill switch if necessary.  

5. **Extend further as needed**  
   Add more safety logic or actions for domain-specific requirements.  

## Goal
*AI Kill Switch* should feel effortless:  
- **Developers** stay focused on building great AI features.  
- **Operators** gain simple, powerful tools to keep AI safe and under control.  
- **AI Service Users** gain confidence knowing the AI they interact with is safe and trustworthy.
