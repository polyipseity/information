import dev.technici4n.fasttransferlib.api.context.Context;
import dev.technici4n.fasttransferlib.impl.context.TransactionContext;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.NoSuchElementException;
import java.util.Random;

public final class GlobalTransferTransaction {
    private static final Deque<GlobalTransactionImpl> DEQUE = new ArrayDeque<>(16);
    
    private GlobalTransferTransaction() {
        throw new AssertionError();
    }

    public static Context open() {
        GlobalTransactionImpl opened = new GlobalTransactionImpl(1L);
        DEQUE.push(opened);
        return opened;
    }

    public static void commit()
            throws NoSuchElementException {
        GlobalTransactionImpl current = DEQUE.pop(); // throws NoSuchElementException if there is nothing
        GlobalTransactionImpl parent = DEQUE.poll();
        DEQUE.push(current);
        if (parent == null) // not nested
            current.commit();
        else // nested
            current.commitWith(parent);
    }

    private static class GlobalTransactionImpl
            extends TransactionContext {
        public GlobalTransactionImpl(long estimatedActions) {
            super(estimatedActions);
        }

        @Override
        public void close() {
            super.close();
            boolean result = DEQUE.removeFirstOccurrence(this);
            assert result; // assert that this was on the stack
        }
    }

    private static class Example {
        static {
            try (Context outermost = open()) {
                outermost.configure(() -> {}, () -> {});

                try (Context intermediate = open()) {
                    intermediate.configure(() -> {}, () -> {});

                    try (Context innermost = open()) {
                        innermost.configure(() -> {}, () -> {});
                        innermost.execute(() -> {});
                        commit();
                    }

                    intermediate.execute(() -> {});

                    if (new Random().nextBoolean())
                        commit();
                }
                commit();
            }
        }
    }
}
